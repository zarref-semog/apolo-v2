from rest_framework import serializers
from .models import PalletInfo

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalletInfo
        fields = '__all__'
