from django.contrib import admin
from inoperate.models import Person
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(Person)