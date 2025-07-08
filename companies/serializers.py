from rest_framework import serializers
from .models import Company, ProductionLine

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
            'status',
            'production-lines',
        ]

class ProductionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLine
        fields = '__all__'

    def validate(self, data):
        company = data.get("company")
        name = data.get("name")

        if self.instance:
            # Atualização: ignora o próprio registro
            if ProductionLine.objects.filter(company=company, name=name).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Já existe uma linha com esse nome para esta empresa.")
        else:
            # Criação
            if ProductionLine.objects.filter(company=company, name=name).exists():
                raise serializers.ValidationError("Já existe uma linha com esse nome para esta empresa.")

        return data