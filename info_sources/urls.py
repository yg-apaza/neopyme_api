from rest_framework import routers

from .views import (
    SunatViewSet, RequestViewSet, ProductsViewSet, PurposeViewSet,
    InfocorpDebtViewSet, AnnualIncomesViewSet
)


app_name = "info-sources"

default_router = routers.DefaultRouter()
default_router.register(r'sunat', SunatViewSet)
default_router.register(r'request', RequestViewSet)
default_router.register(r'products', ProductsViewSet)
default_router.register(r'purposes', PurposeViewSet)
default_router.register(r'infocorps', InfocorpDebtViewSet)
default_router.register(r'annual_incomes', AnnualIncomesViewSet)

urlpatterns = default_router.urls
