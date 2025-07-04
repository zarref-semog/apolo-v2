from rest_framework import viewsets, permissions
from .models import PalletInfo, ReleasedPallet, OnHoldPallet, RejectedPallet
from .serializers import PalletSerializer, ReleasedPalletSerializer, OnHoldPalletSerializer, RejectedPalletSerializer

class PalletInfoViewSet(viewsets.ModelViewSet):
    queryset = PalletInfo.objects.all()
    serializer_class = PalletSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReleasedPallet(viewsets.ModelViewSet):
    queryset = ReleasedPallet.objects.all()
    serializer_class = ReleasedPalletSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OnHoldPalletPallet(viewsets.ModelViewSet):
    queryset = OnHoldPallet.objects.all()
    serializer_class = OnHoldPalletSerializer
    permission_classes = [permissions.IsAuthenticated]

class RejectedPallet(viewsets.ModelViewSet):
    queryset = RejectedPallet.objects.all()
    serializer_class = RejectedPalletSerializer
    permission_classes = [permissions.IsAuthenticated]