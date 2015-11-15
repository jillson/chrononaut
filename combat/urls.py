"""chrononaut combat URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.views.generic import TemplateView
from .views import CombatView

urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$',CombatView.as_view(),name="combat"),
    #url(r'^',TemplateView.as_view(template_name="combat/battle.html"),name="main-combat")
]
