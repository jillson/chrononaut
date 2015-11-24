from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from adventure.models import AdventureInstance,UnlockStatus,Adventure

class CombatView(UpdateView):
    model = AdventureInstance
    fields = []
    template_name = "combat/battle.html"
    def get_success_url(self):
        completedState = UnlockStatus.objects.get(Value="completed")
        unlockedState = UnlockStatus.objects.get(Value="new")
        if not self.object.State or self.object.State.Value != "completed":
            self.object.State = UnlockStatus.objects.get(Value="completed")
            self.object.save()
            newObjects = Adventure.objects.filter(UnlockTrigger=self.object.Adventure)
            for adv in newObjects:
                advInst = AdventureInstance.objects.filter(Adventure=adv,Player=self.object.Player).count()
                if not advInst:
                    advInst = AdventureInstance.objects.create(Adventure=adv,Player=self.object.Player,State=unlockedState)
                    advInst.save()
        return "/"
