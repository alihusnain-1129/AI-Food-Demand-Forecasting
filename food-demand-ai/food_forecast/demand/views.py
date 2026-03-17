from django.shortcuts import render, redirect
from .predictor import predict_next_week, predict_next_day
from .models import Prediction, FoodSales
import json
import pandas as pd


def predict_view(request):
    next_day = None
    next_week = None

    if request.method == "POST":

        # --- collect data ---
        data = {
            'week': int(request.POST.get("week")),
            'center_id': int(request.POST.get("center_id")),
            'meal_id': int(request.POST.get("meal_id")),
            'checkout_price': float(request.POST.get("checkout_price")),
            'base_price': float(request.POST.get("base_price")),
            'emailer_for_promotion': int(request.POST.get("emailer_for_promotion")),
            'homepage_featured': int(request.POST.get("homepage_featured")),
            'city_code': int(request.POST.get("city_code")),
            'region_code': int(request.POST.get("region_code")),
            'op_area': float(request.POST.get("op_area")),
        }

        # --- encode categorical variables ---
        categories = [
            'Beverages','Biryani','Desert','Extras','Fish',
            'Other Snacks','Pasta','Pizza','Rice Bowl',
            'Salad','Sandwich','Seafood','Soup','Starters'
        ]
        for c in categories:
            data[f'category_{c}'] = 1 if c == request.POST.get("category") else 0

        cuisines = ['Continental','Indian','Italian','Thai']
        for c in cuisines:
            data[f'cuisine_{c}'] = 1 if c == request.POST.get("cuisine") else 0

        center_types = ['TYPE_A','TYPE_B','TYPE_C']
        for c in center_types:
            data[f'center_type_{c}'] = 1 if c == request.POST.get("center_type") else 0

        # --- make predictions ---
        next_day = predict_next_day(data)
        next_week = predict_next_week(next_day)

        # --- save prediction to DB ---
        from .views import save_prediction  
        save_prediction(predicted_orders=next_day, model_name="XGBoost_Day", input_data=data)
        save_prediction(predicted_orders=next_week, model_name="XGBoost_Week", input_data=data)
    return render(request, "predict.html", {
        "next_day": next_day,
        "next_week": next_week
    })

def dashboard(request):

    sales = FoodSales.objects.all()

    labels = [f"Week {s.week} - Center {s.center_id}" for s in sales]
    data = [s.orders for s in sales]

    pred_data = [p.predicted_orders for p in Prediction.objects.all()]

    context = {

        "labels":json.dumps(labels),
        "data":json.dumps(data),
        "pred_data": json.dumps(pred_data),
        "predictions":Prediction.objects.all()

    }

    return render(request,"dashboard.html",context)


def upload_csv(request):

    if request.method == "POST":

        file = request.FILES["file"]
        df = pd.read_csv(file)

        for _, row in df.iterrows():

            FoodSales.objects.create(

                week=row["week"],
                center_id=row["center_id"],
                meal_id=row["meal_id"],
                checkout_price=row["checkout_price"],
                base_price=row["base_price"],
                emailer_for_promotion=row["emailer_for_promotion"],
                homepage_featured=row["homepage_featured"],
                city_code=row["city_code"],
                region_code=row["region_code"],
                op_area=row["op_area"],
                category=row["category"],
                cuisine=row["cuisine"],
                center_type=row["center_type"],
                orders=row["num_orders"]

            )

        return redirect("dashboard")

    return render(request,"upload.html")

def save_prediction(predicted_orders, model_name, input_data=None):
    prediction = Prediction(
        predicted_orders=predicted_orders,
        model_used=model_name,
        input_data=input_data
    )
    prediction.save()
    return prediction