from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    Name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.Name


class ItemType(models.Model):
    Name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.Name
    
class Item(models.Model):
    Name = models.CharField(max_length=100)
    ItemType = models.ForeignKey(ItemType)
    def __unicode__(self):
        return self.Name + "(type=" + self.ItemType.Name + ")"

class ItemInstance(models.Model):
    Item = models.ForeignKey(Item)
    def __unicode__(self):
        return self.Item.Name

    
class Player(models.Model):
    Account = models.ForeignKey(User)
    State = models.ForeignKey(State,null=True,default=None)
    Gold = models.IntegerField(default=0)
    Inventory = models.ManyToManyField(ItemInstance,blank=True)
    def __unicode__(self):
        return unicode(self.Account)
