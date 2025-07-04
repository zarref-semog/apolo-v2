from django.db import models
from django.contrib.auth.models import User
from pallets.models import PalletInfo

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    pallet = models.ForeignKey(PalletInfo, on_delete=models.CASCADE)
    contains_label = models.BooleanField()
    pallet_condition = models.BooleanField()
    boxes_organization = models.BooleanField()
    batch_removal = models.DateTimeField()
    observation = models.TextField()
    correction = models.TextField()
    fraction = models.IntegerField(null=True, blank=True)
    amount_default = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
