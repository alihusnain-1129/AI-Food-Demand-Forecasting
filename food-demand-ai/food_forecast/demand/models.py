from django.db import models


class FoodSales(models.Model):

    week = models.IntegerField()
    center_id = models.IntegerField(null=True, blank=True)
    meal_id = models.IntegerField()

    checkout_price = models.FloatField()
    base_price = models.FloatField()

    emailer_for_promotion = models.IntegerField()
    homepage_featured = models.IntegerField()

    city_code = models.IntegerField()
    region_code = models.IntegerField()

    op_area = models.FloatField()

    category = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    center_type = models.CharField(max_length=50, null=True, blank=True)

    orders = models.IntegerField()

class Prediction(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    predicted_orders = models.IntegerField()
    model_used = models.CharField(max_length=50)

    input_data = models.JSONField(null=True, blank=True) 