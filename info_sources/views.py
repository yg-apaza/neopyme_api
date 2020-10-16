import requests

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import EntityInformation
from .serializers import EntityInformationModelSerializer
from .constants import SourcesManager


class SunatViewSet(ModelViewSet):
    queryset = EntityInformation.objects.all()
    serializer_class = EntityInformationModelSerializer
    permission_classes = []
    lookup_field = "ruc"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ruc = instance.ruc
        sunat_info = requests.get(SourcesManager.SUNAT_API + ruc).json()
        # serializer = self.get_serializer(instance)
        # data = serializer.data

        return Response(sunat_info)
