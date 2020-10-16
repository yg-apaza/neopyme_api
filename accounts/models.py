from django.db import models
from django.contrib.auth.models import AbstractUser


class PymeUser(AbstractUser):
    """
    Model for a Pyme account
    """

    email = models.EmailField(
        verbose_name='correo', max_length=255, unique=True)

    class Meta:
        verbose_name = "Pyme"

