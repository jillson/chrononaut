from django.db import models

class Adventure(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()



class UnlockStatus(models.Model):
    
