from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import PymeUser


@admin.register(PymeUser)
class PymeUserAdmin(UserAdmin):
    """
    Admin model for registering a Pyme
    """
    pass
