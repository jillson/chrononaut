from django.conf.urls import include, url

from .views import MapView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$',MapView.as_view(),name="map"),
]
