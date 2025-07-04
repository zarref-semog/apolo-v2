from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Event(models.Model):
    dispatcher = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='events')
    action = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
