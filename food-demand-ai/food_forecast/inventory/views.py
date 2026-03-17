raw_materials_per_meal = {
    'Beverages': {'Water': 250, 'Sugar': 20, 'Flavor/Syrup': 10},
    'Rice Bowl': {'Rice': 200, 'Vegetables': 100, 'Sauce': 30},
    'Starters': {'Chicken': 120, 'Oil': 30, 'Spices': 10},
    'Pasta': {'Pasta': 150, 'Sauce': 80, 'Cheese': 40},
    'Sandwich': {'Bread': 2, 'Chicken/Vegetables': 100, 'Sauce': 20},
    'Biryani': {'Rice': 250, 'Chicken': 150, 'Spices': 20},
    'Pizza': {'Flour': 120, 'Cheese': 80, 'Sauce': 40},
    'Seafood': {'Fish/Shrimp': 180, 'Oil': 40, 'Spices': 15},
    'Desert': {'Milk': 200, 'Sugar': 50, 'Cream': 40},
    'Soup': {'Vegetables': 120, 'Water/Stock': 250, 'Spices': 10},
    'Extras': {'Sauce': 20, 'Bread': 1},
    'Other Snacks': {'Flour': 100, 'Oil': 50, 'Spices': 10},
}

from django.shortcuts import render

def inventory_view(request):
    predicted_demand = {}  # This will store user input or model prediction
    total_materials = {}

    if request.method == "POST":
        # Example: user submits predicted demand per category
        for category in raw_materials_per_meal.keys():
            qty = int(request.POST.get(category, 0))
            predicted_demand[category] = qty

            # Calculate raw materials
            for material, amount_per_meal in raw_materials_per_meal[category].items():
                total_materials[material] = total_materials.get(material, 0) + amount_per_meal * qty

    return render(request, 'inventory/inventory.html', {
        'categories': raw_materials_per_meal.keys(),
        'predicted_demand': predicted_demand,
        'total_materials': total_materials
    })