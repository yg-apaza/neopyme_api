from django.db import models


class EntityInformation(models.Model):
    ruc = models.CharField('ruc', max_length=15)

    class Meta:
        verbose_name = "Información de entidad"
        verbose_name_plural = "Información de entidades"

    def __str__(self):
        return "{}".format(self.ruc)
