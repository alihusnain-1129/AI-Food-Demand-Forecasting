import random

import joblib
import pandas as pd

xgb_model = joblib.load("models/xgboost.pkl")
arima_model = joblib.load("models/arima.pkl")

FEATURE_COLUMNS = [
'week','center_id','meal_id','checkout_price','base_price',
'emailer_for_promotion','homepage_featured','city_code','region_code','op_area',
'category_Beverages','category_Biryani','category_Desert','category_Extras','category_Fish',
'category_Other Snacks','category_Pasta','category_Pizza','category_Rice Bowl','category_Salad',
'category_Sandwich','category_Seafood','category_Soup','category_Starters',
'cuisine_Continental','cuisine_Indian','cuisine_Italian','cuisine_Thai',
'center_type_TYPE_A','center_type_TYPE_B','center_type_TYPE_C'
]

def predict_next_day(data):

    df = pd.DataFrame([data])
    df = df[FEATURE_COLUMNS]

    result = xgb_model.predict(df)

    return int(result[0])


def predict_next_week(next_day_result):

    total = 0

    for i in range(7):
        variation = random.randint(-20, 20)
        total += next_day_result + variation

    return total