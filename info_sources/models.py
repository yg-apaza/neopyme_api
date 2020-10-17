from django.db import models


class EntityInformation(models.Model):
    ruc = models.CharField("ruc", max_length=15)

    class Meta:
        verbose_name = "Información de entidad"
        verbose_name_plural = "Información de entidades"

    def __str__(self):
        return "{}".format(self.ruc)


class Requirement(models.Model):
    alias = models.CharField("Alias", max_length=30, unique=True)
    description = models.TextField("Descripción")
    required = models.BooleanField("¿Es obligatorio?", default=False)

    class Meta:
        verbose_name = "Requisito"


class FinancialProduct(models.Model):
    name = models.CharField("Título", max_length=60)
    description = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    features = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Producto financiero"


class Petitioner(models.Model):
    DNI = "1"
    DOCUMENT_TYPE_CHOICES = [
        (DNI, "DNI"),
    ]
    CLIENT = "1"
    NO_CLIENT = "2"

    ruc = models.CharField("Ruc", max_length=11)
    document_number = models.CharField("Número de documento", max_length=8)
    document_type = models.CharField(
        "Tipo de documento", max_length=1, default=DNI,
        choices=DOCUMENT_TYPE_CHOICES
    )
    email = models.EmailField("Correo", null=True, blank=True)
    phone = models.CharField("Teléfono/Celular", max_length=31, blank=True)
    internal_client = models.BooleanField("¿Ya es cliente?", default=False)

    class Meta:
        verbose_name = "Solicitante"


class Purpose(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        verbose_name = "Propósito"


class RequestedFinantialProduct(models.Model):
    REJECTED_STATUS = "0"
    CONSULTED_STATUS = "1"
    PRE_APPROVED_STATUS = "2"
    STATUS_CHOICES = [
        (CONSULTED_STATUS, "Consultado"),
        (PRE_APPROVED_STATUS, "Pre-aprobado"),
        (REJECTED_STATUS, "Rechazado"),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    petitioner = models.ForeignKey(Petitioner, on_delete=models.CASCADE)
    financial_product = models.ForeignKey(
        FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        "Status", max_length=1, default=CONSULTED_STATUS,
        choices=STATUS_CHOICES
    )
    annual_income = models.PositiveIntegerField(null=True, blank=True)
    infocorp_debt = models.PositiveIntegerField(null=True, blank=True)
    purpose_loan = models.ForeignKey(
        Purpose, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Solicitud de Producto"
