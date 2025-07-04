from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'cnpj',
            'company_name',
            'number',
            'cep',
            'address',
            'status'
        ]