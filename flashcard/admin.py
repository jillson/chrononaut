from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import CardGenerator

class CGResource(resources.ModelResource):
    class Meta:
        model = CardGenerator

class CGAdmin(ImportExportModelAdmin):
    resource_class = CGResource
    pass


admin.site.register(CardGenerator,CGAdmin)
