from rest_framework import viewsets, permissions
from .models import Stage, PalletInfo
from .serializers import PalletSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import requests


class PalletInfoViewSet(viewsets.ModelViewSet):
    queryset = PalletInfo.objects.all()
    serializer_class = PalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="create-by-serial")
    def create_by_serial(self, request):
        serial_number = request.data.get("serial_number")
        if not serial_number:
            return Response(
                {"error": "serial_number is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic 9caf0025-fd18-43ee-9b06-38284c3085cc",
        }

        body = {
            "class": "GetPalletInfo",
            "method": "GetPallet",
            "pallet": serial_number,
        }

        try:
            response = requests.post(
                "http://172.21.70.100:7070/rest-secure.php",
                headers=headers,
                json=body,
            )
            response.raise_for_status()
            result = response.json()
        except requests.RequestException as e:
            return Response(
                {"error": "Failed to fetch pallet data.", "detail": str(e)},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        if result.get("status") != "success" or not result.get("data"):
            return Response(
                {"error": "Invalid response from external API."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        pallet_data = result["data"][0]

        # Dados que podem ser criados ou atualizados
        defaults = {
            "quantity": int(pallet_data["Quantity"]),
            "work_order": pallet_data.get("Workorder"),
            "product_code": pallet_data.get("ProductCode"),
            "product_name": pallet_data.get("ProductName"),
            "customer_code": pallet_data.get("CustomerCode"),
            "customer_name": pallet_data.get("CustomerName"),
            "customer_address": " - ".join(pallet_data.get("CustomerAddress", [])),
            "stage": (
                Stage.RETURN
                if pallet_data.get("StatusCode") == "REPROCESS"
                else Stage.INSPECTION
            ),
            "owner": request.user.profile.company,
            "created_by": request.user.profile,
        }

        obj, created = PalletInfo.objects.update_or_create(
            serial_number=serial_number, defaults=defaults
        )

        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
