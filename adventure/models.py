from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Adventure(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()
    Lat = models.CharField(default="-30",max_length=20)
    Lng = models.CharField(default="-30",max_length=20)
    Distance = models.IntegerField(default=1000)
    UnlockTrigger = models.ForeignKey("Adventure",null=True,blank=True)
    def __unicode__(self):
        return self.Name


class UnlockStatus(models.Model):
    Value = models.CharField(max_length=20)
    def __unicode__(self):
        return self.Value

class AdventureInstance(models.Model):
    Adventure = models.ForeignKey(Adventure)
    State = models.ForeignKey(UnlockStatus)
    Player = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.Adventure) + " for " + unicode(self.Player)
    def get_json(self):
        a = self.Adventure
        if self.State.Value == "inprogress":
            stateBasedLink = "combat"
        else:
            stateBasedLink = "travel"
        return {"name": str(a.Name),
                "state": str(self.State.Value),
                "lat": str(a.Lat),
                "lng": str(a.Lng),
                "id": self.id,
                "description": str(a.Description),
                "link": str(reverse(stateBasedLink,args=[self.id]))}


