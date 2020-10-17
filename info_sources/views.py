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
    InfocorpDebt,
    AnnualIncomes,
    RequestedFinantialProduct,
)
from .serializers import (
    EntityInformationModelSerializer,
    RequestCreateSerializer,
    PetitionerSerializer,
    ProductSerializer,
    PurposeSerializer,
    InfocorpDebtSerializer,
    AnnualIncomesSerializer,
)
from .constants import SourcesManager


class PurposeViewSet(ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    permission_classes = []


class InfocorpDebtViewSet(ModelViewSet):
    queryset = InfocorpDebt.objects.all()
    serializer_class = InfocorpDebtSerializer
    permission_classes = []


class AnnualIncomesViewSet(ModelViewSet):
    queryset = AnnualIncomes.objects.all()
    serializer_class = AnnualIncomesSerializer
    permission_classes = []


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
        print('0' * 10)
        if serializer.is_valid(raise_exception=True):
            petitioner, _ = Petitioner.objects.get_or_create(**request.data)
            request = RequestedFinantialProduct.objects.create(
                petitioner=petitioner)
            data = PetitionerSerializer(petitioner).data
            data.update({"id": request.id})
            return Response(data=data, status=200)
        return Response(data=request.data, status=400)



class ProductsViewSet(ModelViewSet):
    queryset = FinancialProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
