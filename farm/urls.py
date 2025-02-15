from django.urls import path,include
from . import views



urlpatterns=[

    path("", views.home, name="home"),
    path("features/", views.features, name="features"),
    path("farmer_dashboard/", views.farmer_dashboard, name="farmer_dashboard"),
 


     ############## Farmer ##############
    path("farmer_register", views.farmer_register, name='farmer_register'),
    path("farmer_login", views.farmer_login, name='farmer_login'),
    path('farmer_logout/', views.farmer_logout, name='farmer_logout'),




]