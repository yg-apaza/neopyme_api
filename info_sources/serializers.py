from rest_framework import serializers

from .models import EntityInformation, Petitioner, FinancialProduct


class EntityInformationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityInformation
        fields = ("ruc", )

class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petitioner
        fields = ("ruc", "document_number", "internal_client")

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
        feilds = (
            "id", "name", "description", "benefits", "features", "requirements")