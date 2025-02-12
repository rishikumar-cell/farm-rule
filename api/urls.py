from django.urls import path
from . import views

urlpatterns=[
    path("get/", views.get_farmer_data),
    path("add/", views.add_farmer_data),


]