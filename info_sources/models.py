from django.db import models

from jsonfield import JSONField


class EntityInformation(models.Model):
    OTHER = "0"
    SUNAT = "1"
    OSCE = "2"
    SOURCE_CHOICES = [
        (SUNAT, "Sunat"),
        (OSCE, "Osce"),
        (OTHER, "Otra")
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ruc = models.CharField("ruc", max_length=15)
    source = models.CharField(
        "Fuente", max_length=2, choices=SOURCE_CHOICES, blank=True)
    link = models.CharField("Link", blank=True, max_length=255)
    data = JSONField(blank=True)

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
    completed_register = models.BooleanField("Registro completo", default=False)

    class Meta:
        verbose_name = "Solicitante"


class Purpose(models.Model):
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Propósito"


class InfocorpDebt(models.Model):
    text = models.CharField("texto", max_length=255)

    class Meta:
        verbose_name = "Deuda Infocorp"
        verbose_name_plural = "Deudas Infocorp"


class AnnualIncomes(models.Model):
    text = models.CharField("texto", max_length=255)

    class Meta:
        verbose_name = "Facturación anual"
        verbose_name_plural = "Facturaciones anuales"


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
    annual_income = models.ForeignKey(
        AnnualIncomes, null=True, blank=True, on_delete=models.CASCADE)
    infocorp_debt = models.ForeignKey(
        InfocorpDebt, null=True, blank=True, on_delete=models.CASCADE)
    purpose_loan = models.ForeignKey(
        Purpose, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Solicitud de Producto"
