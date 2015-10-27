from django.db import models
from core.models import ItemInstance,Item
import random


class Class_Action(models.Model):
    Name = models.CharField(max_length=100)
    #more to come
    def __unicode__(self):
        return self.Name

class Character_Class(models.Model):
    Name = models.CharField(max_length=100)
    Actions = models.ManyToManyField(Class_Action,blank=True)
    #more to come
    def __unicode__(self):
        return self.Name
    
class PC(models.Model):
    Name = models.CharField(max_length=100,default="Sammy Do!")
    HP = models.IntegerField()
    HP_Max = models.IntegerField()
    PClass = models.ForeignKey(Character_Class)
    XP = models.IntegerField(default=0)
    Level = models.IntegerField(default=1)
    Equipment = models.ManyToManyField(ItemInstance,blank=True)
    Owner = models.ForeignKey("core.Player",null=True)
    Active = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.Name)

    
class BattleGenerator:
    def generate(self,player):
        #For now, keep this simple and just create a couple of the same type
        stick = ItemInstance.objects.create(Item=Item.objects.filter(Name="stick")[0])
        cclass = random.choice(Character_Class.objects.all())
        npcs = [PC.objects.create(Name="Generic Bad Guy #%d"%(i+1),
                                  HP=random.randint(10,16),HP_Max=16,
                                  PClass=cclass) for i in xrange(3)]
        pcs = PC.objects.filter(Owner=player,Active=True)
        b = Battle.objects.create(Name="battle",HumanLead=player)
        for n in npcs:
            n.HP_MAX=n.HP
            n.Equipment.add(stick)
            n.save()
            b.Team2.add(n)
        for p in pcs:
            b.Team1.add(p)
        b.save()
        player.State=State.objects.filter("InBattle")[0]
        player.save()
                                     
    
class Battle(models.Model):
    #TODO: add location etc.
    Name = models.CharField(max_length=80)
    Team1 = models.ManyToManyField(PC,related_name="friends")
    Team2 = models.ManyToManyField(PC,related_name="enemies")
    HumanLead = models.ForeignKey("core.Player")
    def __unicode__(self):
        return self.Name
                                  
                                  
