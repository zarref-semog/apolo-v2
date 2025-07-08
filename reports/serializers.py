from rest_framework import serializers
from .models import WipReport, ReleasedPalletReport, OnHoldPalletReport, RejectedPalletReport

class WipReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WipReport
        fields = '__all__'

class ReleasedPalletReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleasedPalletReport
        fields = '__all__'

class OnHoldPalletReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnHoldPalletReport
        fields = '__all__'

class RejectedPalletReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectedPalletReport
        fields = '__all__'