from django import forms
from .models import FoodSales

class SalesForm(forms.ModelForm):

    class Meta:
        model = FoodSales
        fields = "__all__"