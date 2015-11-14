"""chrononaut travel URL Configuration
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView, DetailView

#TODO: add check that user has actually unlocked a travel route

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="travel/travel.html")),
    url(r'^(?P<pk>[\d]+)/$',DetailView.as_view(template_name="travel/travel.html"),name="travel"),
]
