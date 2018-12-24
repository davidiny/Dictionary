from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name = "index"),
    path('new', views.post_new, name='post_new')
]