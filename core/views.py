from django.shortcuts import render

from django.views.generic.base import TemplateView

from .models import Player, State, ItemType, Item, ItemInstance

from combat.models import BattleGenerator, PC, Character_Class

class HomePageView(TemplateView):

    template_name = "core/home.html"

class SetupView(TemplateView):
    template_name = "core/setup.html"
    
    def get_context_data(self, **kwargs):
        context = super(SetupView, self).get_context_data(**kwargs)
        user = self.request.user
        player, _ = Player.objects.get_or_create(Account=user)
        player.State, created = State.objects.get_or_create(Name="InBattle")
        if created:
            player.State.save()
        player.save()
        pcs = PC.objects.filter(Owner=player, Active=True)
        weaponType, created = ItemType.objects.get_or_create(Name="weapon")
        if created:
            weaponType.save()
        stickType, created = Item.objects.get_or_create(Name="stick",ItemType=weaponType)
        if created:
            stickType.save()
        stick, created = ItemInstance.objects.get_or_create(Item=stickType)
        if created:
            stick.save()
        if len(pcs) < 3:
            fighter, created = Character_Class.objects.get_or_create(Name="fighter")
            if created:
                fighter.save()
            for i in xrange(3 - len(pcs)):
                newpc = PC.objects.create(Name="Joe",HP=10,HP_Max=10,PClass=fighter,Active=True)
                newpc.Equipment.add(stick)
                newpc.save()
        
        bg = BattleGenerator()
        bg.generate(player)
        context["player"] = player
        return context

# Create your views here.
