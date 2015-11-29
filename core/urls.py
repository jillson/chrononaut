"""chrononaut core URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

#from .views import LoginView
from maps.views import MapMainView

urlpatterns = [
    url(r'^$',MapMainView.as_view(template_name="maps/main.html"),name="home"),
    url(r'^login/$',TemplateView.as_view(template_name="core/login.html"),name="login")
]
