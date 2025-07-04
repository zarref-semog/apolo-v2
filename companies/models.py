from django.db import models

class Company(models.Model):
    cnpj = models.CharField(max_length=50, unique=True)
    company_name = models.CharField(max_length=255)
    number = models.IntegerField()
    cep = models.CharField(max_length=50)
    address = models.CharField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
