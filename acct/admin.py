from django.contrib import admin
from .models import NewCustomUser
# Register your models here.

@admin.register( NewCustomUser)
class NewCustomUserAdmin( admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'created']
    prepopulated_fields = {"slug": ("email",)}