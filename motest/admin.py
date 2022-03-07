from django.contrib import admin
from .models import MoTestModel, FileModels

# Register your models here.
@admin.register( MoTestModel)
class LinstMoTestModelAdmin( admin.ModelAdmin):
    list_display = ['id', 'user', 'baby', 'event_date', 'created', 'updated', 'mother', 'father']
    list_editable = ['event_date', 'baby', 'mother', 'father']
    list_filter = ['user', 'event_date', 'baby']
    raw_id_fields = ("photo_first", "photo_sec")

@admin.register( FileModels)
class FileAdmin( admin.ModelAdmin):
    list_display = ['id', 'user', 'files', 'created']
