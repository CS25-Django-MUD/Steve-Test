from django.urls import path
from . import views

# app level url patterns should match the view function handling the logic for the expected output should a user visit that particular url

urlpatterns = [
    #   route, view logic for route, reverse lookup name
    # empty string = home, could also be something like /notes or /home
    # renders these IN ORDER. 
    path('', views.home, name='notes-home'),
    path('about/', views.about, name='notes-about'),
]