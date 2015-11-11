"""chrononaut combat URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView

from .models import CardGenerator
from .views import CardGeneratorJSONView,CardGeneratorSingleView


urlpatterns = [
    url(r'^single/$',CardGeneratorSingleView.as_view(),name="single-card"),
    url(r'^(?P<pk>[\d+])/$',CardGeneratorJSONView.as_view(),name="card-detail"),
    url(r'^$',ListView.as_view(model=CardGenerator),name="card-list")
]
