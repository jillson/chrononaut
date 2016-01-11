from django.shortcuts import render
from django.views.generic import DetailView

from adventure.models import AdventureInstance,Adventure,UnlockStatus

from .models import Map

class MapView(DetailView):
    model = Map
    template_name = "maps/main.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MapView, self).get_context_data(**kwargs)
        ai = AdventureInstance.objects.filter(Player=self.request.user,Adventure__Map=self.object)
        if ai.count() == 0:
            us = UnlockStatus.objects.get(Value="new")
            freeLevels = Adventure.objects.filter(UnlockTrigger=None)
            for f in freeLevels:
                print "Creating new instance for %s of %s" % (str(self.request.user),str(f))
                ai = AdventureInstance.objects.create(Player=self.request.user,Adventure=f,State=us)
                ai.save()
            ai = AdventureInstance.objects.filter(Player=self.request.user,Adventure__Map=self.object)
                
        
        context['adventures'] = "[" + ",\n".join([str(x.get_json()) for x in ai]) + "]"
        return context
