"""chrononaut travel URL Configuration
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="travel/travel.html")),
]
