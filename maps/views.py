from django.shortcuts import render
from django.views.generic import TemplateView

from adventure.models import AdventureInstance

class MapMainView(TemplateView):
    template_name = "maps/main.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MapMainView, self).get_context_data(**kwargs)
        context['adventures'] = "\n".join([str(x.get_json()) for x in AdventureInstance.objects.filter(Player=self.request.user)])
        print "Debug",context['adventures']
        return context
