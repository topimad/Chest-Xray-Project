from django.contrib import admin
from .models import DocumentModel
from .models import DoctorsInfo
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(DocumentModel)

class DocumentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorsInfo)
class DoctorsInfoAdmin(ImportExportModelAdmin):
    pass