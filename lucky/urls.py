from django.urls import path

from . import views



urlpatterns = [
    path('', views.lucky_index, name = "lucky_index")
]