from django.shortcuts import render
from django.views.generic import TemplateView

from adventure.models import AdventureInstance,Adventure,UnlockStatus

class MapMainView(TemplateView):
    template_name = "maps/main.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MapMainView, self).get_context_data(**kwargs)

        ai = AdventureInstance.objects.filter(Player=self.request.user)
        if ai.count() == 0:
            us = UnlockStatus.objects.get(Value="new")
            freeLevels = Adventure.objects.filter(UnlockTrigger=None)
            for f in freeLevels:
                print "Creating new instance for %s of %s" % (str(self.request.user),str(f))
                ai = AdventureInstance.objects.create(Player=self.request.user,Adventure=f,State=us)
                ai.save()
            ai = AdventureInstance.objects.filter(Player=self.request.user)
                
        
        context['adventures'] = "[" + ",\n".join([str(x.get_json()) for x in ai]) + "]"
        return context
