"""chrononaut core URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import SetupView, HomePageView


urlpatterns = [
    url(r'^setup/$',SetupView.as_view(),name="setup"),
    url(r'^$',TemplateView.as_view(template_name="maps/main.html"),name="home")
]
