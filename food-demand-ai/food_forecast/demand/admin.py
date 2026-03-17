from django.contrib import admin
from .models import FoodSales, Prediction

@admin.register(FoodSales)
class FoodSalesAdmin(admin.ModelAdmin):
    list_display = (
        'week', 'center_id', 'meal_id', 'orders', 'checkout_price', 'base_price',
        'city_code', 'region_code', 'category', 'cuisine', 'center_type'
    )
    search_fields = ('city_code', 'region_code', 'category', 'cuisine')
    list_filter = ('week', 'city_code', 'region_code', 'category', 'center_type')
    readonly_fields = ('op_area',)

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('date', 'predicted_orders', 'model_used')
    list_filter = ('date', 'model_used')
    readonly_fields = ('date',)