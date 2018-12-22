import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(action):
    return HttpResponse("Hello, world.  I will include an API soon")

# Create your views here.
