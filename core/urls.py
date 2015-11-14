"""chrononaut core URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import SetupView, HomePageView
from maps.views import MapMainView

urlpatterns = [
    url(r'^setup/$',SetupView.as_view(),name="setup"),
    url(r'^$',MapMainView.as_view(template_name="maps/main.html"),name="home")
]
