from rest_framework import serializers
from .models import PalletInfo, ReleasedPallet, OnHoldPallet, RejectedPallet

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalletInfo
        fields = '__all__'

class ReleasedPalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleasedPallet
        fields = '__all__'

class OnHoldPalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnHoldPallet
        fields = '__all__'

class RejectedPalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectedPallet
        fields = '__all__'