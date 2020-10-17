from rest_framework import routers

from .views import SunatViewSet, RequestViewSet, ProductsViewSet


app_name = "info-sources"

default_router = routers.DefaultRouter()
default_router.register(r'sunat', SunatViewSet)
default_router.register(r'request', RequestViewSet)
default_router.register(r'products', ProductsViewSet)

urlpatterns = default_router.urls
