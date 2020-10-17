from django.contrib import admin

from .models import (
    EntityInformation,
    FinancialProduct,
    Petitioner,
    RequestedFinantialProduct,
)


@admin.register(EntityInformation)
class EntityInformationAdmin(admin.ModelAdmin):
    """
    Admin model for registering a Pyme
    """
    list_display = ('ruc', )


@admin.register(FinancialProduct)
class FinancialProductAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Petitioner)
class PetitionerModelAdmin(admin.ModelAdmin):
    list_display = ("ruc", "document_number", )


@admin.register(RequestedFinantialProduct)
class RequestedFinantialProductModelAdmin(admin.ModelAdmin):
    list_display = ("petitioner", "financial_product", )

