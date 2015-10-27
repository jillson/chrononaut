from django.contrib import admin
from .models import State, ItemType, Item, ItemInstance, Player
# Register your models here.
admin.site.register(State)
admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(ItemInstance)
admin.site.register(Player)
