from django.contrib import admin
from .models import Adventure, AdventureInstance, UnlockStatus
admin.site.register(Adventure)
admin.site.register(AdventureInstance)
admin.site.register(UnlockStatus)

