import requests

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .models import (
    EntityInformation,
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
    RequestUpdateSerializer,
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

        return Response(sunat_info)


class RequestViewSet(ModelViewSet):
    queryset = RequestedFinantialProduct.objects.all()
    serializer_class = RequestUpdateSerializer
    permission_classes = []

    def create(self, request):
        serializer = RequestCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            petitioner, _ = Petitioner.objects.get_or_create(**request.data)
            request = RequestedFinantialProduct.objects.create(
                petitioner=petitioner)
            data = PetitionerSerializer(petitioner).data
            data.update({"id": request.id})
            return Response(data=data, status=200)
        return Response(data=request.data, status=400)

    def partial_update(self, request, pk=None):
        response = super().partial_update(request, pk)
        return response

    


class ProductsViewSet(ModelViewSet):
    queryset = FinancialProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
