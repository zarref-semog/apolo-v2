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


class ProductionLine(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="production_lines")
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["company", "name"], name="unique_line_per_company")
        ]

    def __str__(self):
        return f"{self.name} ({self.company.company_name})"
