from django.contrib import admin

from .models import EntityInformation, FinancialProduct


@admin.register(EntityInformation)
class EntityInformationAdmin(admin.ModelAdmin):
    """
    Admin model for registering a Pyme
    """
    list_display = ('ruc', )

@admin.register(FinancialProduct)
class FinancialProductAdmin(admin.ModelAdmin):
    list_display = ("name", )
