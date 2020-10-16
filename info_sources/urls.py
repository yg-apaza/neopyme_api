from rest_framework import routers

from .views import SunatViewSet


app_name = "info-sources"

default_router = routers.DefaultRouter()
default_router.register(r'sunat', SunatViewSet)

urlpatterns = default_router.urls
