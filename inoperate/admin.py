from django.contrib import admin
from inoperate.models import Person
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PersonAdmin(ImportExportModelAdmin):
    list_display=['account_number','name','amount']

admin.site.register(Person, PersonAdmin)