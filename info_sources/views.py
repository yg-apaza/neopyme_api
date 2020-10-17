import requests

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .models import (
    EntityInformation,
    Requirement,
    FinancialProduct,
    Petitioner,
    Purpose,
    RequestedFinantialProduct,
)
from .serializers import (
    EntityInformationModelSerializer,
    RequestCreateSerializer,
    PetitionerSerializer,
    ProductSerializer,
)
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

class RequestViewSet(ViewSet, CreateModelMixin):
    queryset = RequestedFinantialProduct.objects.all()
    serializer_class = None
    permission_classes = []

    def create(self, request):
        serializer = RequestCreateSerializer(data=request.data)
        if serializer.is_valid():
            petitioner = Petitioner.objects.get_or_create(**request.data)
            request = RequestedFinantialProduct.objects.create(
                petitioner=petitioner)
            data = PetitionerSerializer(petitioner).data
            data.update({"id": request.id})
            return Response(data=data, status=200)

        return Response(data=data, status=200)



class ProductsViewSet(ViewSet, ListModelMixin):
    queryset = FinancialProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
