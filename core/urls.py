"""chrononaut core URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

#from .views import LoginView
from .views import HQView

urlpatterns = [
    url(r'^$',HQView.as_view(),name="home"),
]
