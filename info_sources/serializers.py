import requests

from rest_framework import serializers

from .models import (
    EntityInformation,
    Petitioner,
    FinancialProduct,
    InfocorpDebt,
    AnnualIncomes,
    Purpose,
    RequestedFinantialProduct,
)
from .constants import SourcesManager


class EntityInformationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityInformation
        fields = ("ruc", )

class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petitioner
        fields = ("ruc", "document_number",)

    def validate(self, data):
        ruc = data['ruc']
        dni = data['document_number']
        sunat_info = requests.get(SourcesManager.SUNAT_API + ruc).json()
        legal_owners = sunat_info.get("representante_legal")
        valid_dnis = [x for x in legal_owners.keys()]
        valid = False
        for valid_dni in valid_dnis:
            if dni in valid_dni:
                valid = True
                break
        print(valid_dnis)
        if valid:
            return data 
        else:
            raise serializers.ValidationError(
                "El DNI no corresponde a un representante legal")
        

class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedFinantialProduct
        fields = ("annual_income", "infocorp_debt", "purpose_loan", )


class PetitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petitioner
        fields = ("ruc", "document_number", )

class ProductSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    benefits = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    
    def get_description(self, obj):
        return obj.description.splitlines()
    
    def get_benefits(self, obj):
        return obj.benefits.splitlines()

    def get_features(self, obj):
        return obj.features.splitlines()

    def get_requirements(self, obj):
        return obj.requirements.splitlines()
    class Meta:
        model = FinancialProduct
        fields = (
            "id", "name", "description", "benefits", "features", "requirements")


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('id', 'text')


class InfocorpDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfocorpDebt
        fields = ('id', 'text')


class AnnualIncomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualIncomes
        fields = ('id', 'text')


