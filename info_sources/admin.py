from django.contrib import admin

from .models import (
    EntityInformation,
    FinancialProduct,
    Petitioner,
    RequestedFinantialProduct,
    Purpose,
    InfocorpDebt,
    AnnualIncomes,
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
    list_display = ("ruc", "document_type", "document_number", )


@admin.register(RequestedFinantialProduct)
class RequestedFinantialProductModelAdmin(admin.ModelAdmin):
    list_display = ("petitioner", "financial_product", )


@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ("text", )


@admin.register(InfocorpDebt)
class InfocorpDebtAdmin(admin.ModelAdmin):
    list_display = ("text", )


@admin.register(AnnualIncomes)
class AnnualIncomesAdmin(admin.ModelAdmin):
    list_display = ("text", )
