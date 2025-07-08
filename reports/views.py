from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from minio import Minio
import os
from core import settings
from .models import WipReport, ReleasedPalletReport, OnHoldPalletReport, RejectedPalletReport
from .serializers import WipReportSerializer, ReleasedPalletReportSerializer, OnHoldPalletReportSerializer, RejectedPalletReportSerializer

def get_minio_client():
    conf = settings.MINIO_STORAGE
    return Minio(
        conf['ENDPOINT'],
        access_key=conf['ACCESS_KEY'],
        secret_key=conf['SECRET_KEY'],
        secure=conf['SECURE'],
    )


class WipReportViewSet(viewsets.ModelViewSet):
    queryset = WipReport.objects.all()
    serializer_class = WipReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="upload-images")
    def upload_images(self, request, pk=None):
        report = self.get_object()
        files = request.FILES.getlist("images")

        if not files:
            return Response({"error": "No images provided."}, status=status.HTTP_400_BAD_REQUEST)

        client = get_minio_client()
        bucket = settings.MINIO_STORAGE['BUCKET']
        company = report.pallet.owner.cnpj

        urls = []

        for file in files:
            ext = os.path.splitext(file.name)[-1] or ".jpg"
            unique_name = f"{uuid.uuid4()}{ext}"
            object_path = f"{company}/reports/wip-reports/{unique_name}"

            client.put_object(
                bucket_name=bucket,
                object_name=object_path,
                data=file.file,
                length=file.size,
                content_type=file.content_type,
            )

            url = f"http{'s' if settings.MINIO_STORAGE['SECURE'] else ''}://{settings.MINIO_STORAGE['ENDPOINT']}/{bucket}/{object_path}"
            urls.append(url)

        # Atualiza o campo JSON
        report.image_urls.extend(urls)
        report.save()

        return Response({"image_urls": report.image_urls}, status=status.HTTP_200_OK)

class ReleasedPalletReportViewSet(viewsets.ModelViewSet):
    queryset = ReleasedPalletReport.objects.all()
    serializer_class = ReleasedPalletReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="upload-images")
    def upload_images(self, request, pk=None):
        report = self.get_object()
        files = request.FILES.getlist("images")

        if not files:
            return Response({"error": "No images provided."}, status=status.HTTP_400_BAD_REQUEST)

        client = get_minio_client()
        bucket = settings.MINIO_STORAGE['BUCKET']
        company = report.pallet.owner.cnpj

        urls = []

        for file in files:
            ext = os.path.splitext(file.name)[-1] or ".jpg"
            unique_name = f"{uuid.uuid4()}{ext}"
            object_path = f"{company}/reports/released-pallet-reports/{unique_name}"

            client.put_object(
                bucket_name=bucket,
                object_name=object_path,
                data=file.file,
                length=file.size,
                content_type=file.content_type,
            )

            url = f"http{'s' if settings.MINIO_STORAGE['SECURE'] else ''}://{settings.MINIO_STORAGE['ENDPOINT']}/{bucket}/{object_path}"
            urls.append(url)

        # Atualiza o campo JSON
        report.image_urls.extend(urls)
        report.save()

        return Response({"image_urls": report.image_urls}, status=status.HTTP_200_OK)


class OnHoldPalletReportViewSet(viewsets.ModelViewSet):
    queryset = OnHoldPalletReport.objects.all()
    serializer_class = OnHoldPalletReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="upload-images")
    def upload_images(self, request, pk=None):
        report = self.get_object()
        files = request.FILES.getlist("images")

        if not files:
            return Response({"error": "No images provided."}, status=status.HTTP_400_BAD_REQUEST)

        client = get_minio_client()
        bucket = settings.MINIO_STORAGE['BUCKET']
        company = report.pallet.owner.cnpj

        urls = []

        for file in files:
            ext = os.path.splitext(file.name)[-1] or ".jpg"
            unique_name = f"{uuid.uuid4()}{ext}"
            object_path = f"{company}/reports/on-hold-pallet-reports/{unique_name}"

            client.put_object(
                bucket_name=bucket,
                object_name=object_path,
                data=file.file,
                length=file.size,
                content_type=file.content_type,
            )

            url = f"http{'s' if settings.MINIO_STORAGE['SECURE'] else ''}://{settings.MINIO_STORAGE['ENDPOINT']}/{bucket}/{object_path}"
            urls.append(url)

        # Atualiza o campo JSON
        report.image_urls.extend(urls)
        report.save()

        return Response({"image_urls": report.image_urls}, status=status.HTTP_200_OK)


class RejectedPalletReportViewSet(viewsets.ModelViewSet):
    queryset = RejectedPalletReport.objects.all()
    serializer_class = RejectedPalletReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="upload-images")
    def upload_images(self, request, pk=None):
        report = self.get_object()
        files = request.FILES.getlist("images")

        if not files:
            return Response({"error": "No images provided."}, status=status.HTTP_400_BAD_REQUEST)

        client = get_minio_client()
        bucket = settings.MINIO_STORAGE['BUCKET']
        company = report.pallet.owner.cnpj

        urls = []

        for file in files:
            ext = os.path.splitext(file.name)[-1] or ".jpg"
            unique_name = f"{uuid.uuid4()}{ext}"
            object_path = f"{company}/reports/rejected-pallet-reports/{unique_name}"

            client.put_object(
                bucket_name=bucket,
                object_name=object_path,
                data=file.file,
                length=file.size,
                content_type=file.content_type,
            )

            url = f"http{'s' if settings.MINIO_STORAGE['SECURE'] else ''}://{settings.MINIO_STORAGE['ENDPOINT']}/{bucket}/{object_path}"
            urls.append(url)

        # Atualiza o campo JSON
        report.image_urls.extend(urls)
        report.save()

        return Response({"image_urls": report.image_urls}, status=status.HTTP_200_OK)
