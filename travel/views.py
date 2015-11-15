from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from adventure.models import AdventureInstance,UnlockStatus

class TravelView(UpdateView):
    model = AdventureInstance
    fields = []
    template = "travel/travel.html"
    def get_success_url(self):
        self.object.State = UnlockStatus.objects.get(Value="inprogress")
        self.object.save()
        return reverse("combat",args=[self.object.id])
