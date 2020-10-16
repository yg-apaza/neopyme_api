from django.contrib import admin

from .models import EntityInformation


@admin.register(EntityInformation)
class EntityInformationAdmin(admin.ModelAdmin):
    """
    Admin model for registering a Pyme
    """
    list_display = ('ruc',)

