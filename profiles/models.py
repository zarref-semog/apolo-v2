from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Role(models.TextChoices):
    GENERAL_MANAGER = "GENERAL_MANAGER", "General Manager"
    MANAGER = "MANAGER", "Manager"
    EMPLOYEE = "EMPLOYEE", "Employee"
    WAREHOUSE = "WAREHOUSE", "Warehouse"

class Profile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Role.choices)
    registry = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['company', 'registry'], name='unique_registry_per_company')
        ]

    def has_company_access(self, company_id):
        if self.role == Role.GENERAL_MANAGER:
            return True
        if self.role in [Role.MANAGER, Role.EMPLOYEE] and self.company:
            return self.company.id == company_id
        return False

