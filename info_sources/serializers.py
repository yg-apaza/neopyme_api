from rest_framework import serializers

from .models import EntityInformation


class EntityInformationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityInformation
        fields = ('ruc', )
