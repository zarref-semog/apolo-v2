from rest_framework import viewsets, permissions
from .models import Company, ProductionLine
from .serializers import CompanySerializer, ProductionLineSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductionLineViewSet(viewsets.ModelViewSet):
    queryset = ProductionLine.objects.all()
    serializer_class = ProductionLineSerializer
    permission_classes = [permissions.IsAuthenticated]
