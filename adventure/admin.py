from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User

from .models import Adventure, AdventureInstance, UnlockStatus

class AdventureResource(resources.ModelResource):
    class Meta:
        model = Adventure
    def after_save_instance(self, instance, dry_run):
        # update AdventureInstances if the newly added Adventures are now unlocked
        if not dry_run: #TODO: should we do something on dry runs?
            newState = UnlockStatus.objects.get(Value="new")
            ut = instance.UnlockTrigger
            if ut: # this possibly new adventure has an unlock requirement
                for u in User.objects.all():
                    ai = AdventureInstance.objects.filter(Adventure=ut,Player=u)
                    if len(ai) > 0 and ai[0].State.Value == "completed":
                        ai2 = AdventureInstance.objects.filter(Adventure=instance,Player=u)
                        if len(ai2) == 0: #Newly unlocked mission:
                            ai2 = AdventureInstance.objects.create(Adventure=instance,Player=u,State=newState)
                            ai2.save()
            else:
                for u in User.objects.all():
                    ai2 = AdventureInstance.objects.filter(Adventure=instance,Player=u)
                    if len(ai2) == 0: #Newly unlocked mission:
                        ai2 = AdventureInstance.objects.create(Adventure=instance,Player=u,State=newState)
                        ai2.save()                            
                
        
class AdventureAdmin(ImportExportModelAdmin):
    resource_class = AdventureResource
    pass


admin.site.register(Adventure,AdventureAdmin)
admin.site.register(AdventureInstance)
admin.site.register(UnlockStatus)

