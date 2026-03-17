from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/',views.dashboard,name='dashboard'),

    path('predict/',views.predict_view,name='predict'),

    path('upload/',views.upload_csv,name='upload'),

]