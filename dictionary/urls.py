"""dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views as flat_views

urlpatterns = [
    path('examples/', include('examples.urls')),
    path('definitions/', include('definitions.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('lucky/', include('lucky.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('pages/pricing/', flat_views.flatpage, {'url': '/pages/pricing/'}, name='pricing'),
    path('pages/about/', flat_views.flatpage, {'url': '/pages/about/'}, name='about'),
]