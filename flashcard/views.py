import random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.detail import DetailView
from .models import CardGenerator


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        return context["object"].get_json()

class JSONDetailView(DetailView, JSONResponseMixin):
    def render_to_response(self, context, **kwargs):
        return self.render_to_json_response(context, **kwargs)
    

class CardGeneratorJSONView(JSONDetailView):
    model = CardGenerator
    #def get_context_data(self, **kwargs):
    #    context = super(CardGeneratorJSONView, self).get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context


class CardGeneratorSingleView(View):
    def get(self, request, *args, **kwargs):
        print "Debug",args,kwargs
        #TODO: add optional parameters to select by level etc.
        cgs = CardGenerator.objects.all()
        cg = random.choice(cgs)
        return JsonResponse(cg.get_json())


