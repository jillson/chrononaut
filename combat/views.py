from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from adventure.models import AdventureInstance,UnlockStatus

class CombatView(UpdateView):
    model = AdventureInstance
    fields = []
    template_name = "combat/battle.html"
    def get_success_url(self):
        self.object.State = UnlockStatus.objects.get(Value="completed")
        self.object.save()
        return "/"
