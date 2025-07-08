from django.db import models
from companies.models import Company
from django.contrib.auth.models import User

class Stage(models.TextChoices):
    INSPECTION = "INSPECTION", "Inspection"
    WIP = "WIP", "Work In Progress"
    STORAGE = "STORAGE", "Storage"
    RETURN = "RETURN", "Return"
    FINISHED = "FINISHED", "Finished"

class PalletInfo(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="pallets")
    serial_number = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    work_order = models.CharField(max_length=50, null=True, blank=True)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=255)
    stage = models.CharField(max_length=50, choices=Stage.choices)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_pallets")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pallet {self.serial_number} ({self.product_name})"