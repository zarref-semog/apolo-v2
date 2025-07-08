from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Event(models.Model):
    dispatcher = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='events')
    action = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.action}"
