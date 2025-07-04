from django.db import models

class Invoice(models.Model):
    identifier = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255, unique=True)
    state_registration = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    value = models.FloatField()
    purchase_order = models.CharField(max_length=255, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    batch = models.OneToOneField("Batch", on_delete=models.SET_NULL, null=True, blank=True, related_name="invoice_ref")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InvoiceReport(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    approved = models.BooleanField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inconsistency(models.Model):
    field = models.CharField(max_length=255)
    expected = models.FloatField()
    received = models.FloatField()
    invoice_report = models.ForeignKey("InvoiceReport", on_delete=models.CASCADE)
