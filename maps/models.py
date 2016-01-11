from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Map(models.Model):
    Name = models.CharField(max_length=20)
    Attribution = models.TextField()
    Filename = models.CharField(max_length=40)
    UnlockAmount = models.IntegerField(default=0)
    def __unicode__(self):
        return self.Name
