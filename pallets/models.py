from django.db import models
from companies.models import Company
from django.contrib.auth.models import User

class Stage(models.TextChoices):
    INSPECTION = "INSPECTION", "Inspection"
    WIP = "WIP", "Work In Progress"
    STORAGE = "STORAGE", "Storage"
    RETURN = "RETURN", "Return"
    FINISHED = "FINISHED", "Finished"

class HoldReason(models.TextChoices):
    AGUARDANDO_AGIN_DAT = "AGUARDANDO_AGIN_DAT", "Aguardando AGIN/DAT"
    AGUARDANDO_OP = "AGUARDANDO_OP", "Aguardando OP"
    AGUARDANDO_DESVIO_ENGENHARIA = "AGUARDANDO_DESVIO_ENGENHARIA", "Aguardando Desvio de Engenharia"
    AGUARDANDO_RESULTADO_ORT = "AGUARDANDO_RESULTADO_ORT", "Aguardando Resultado ORT"
    OUTROS = "OUTROS", "Outros"

class Step(models.TextChoices):
    REVISAO_PRODUCAO = "REVISAO_PRODUCAO", "Revisão Produção"
    REINSPECAO_QUALIDADE = "REINSPECAO_QUALIDADE", "Reinspeção Qualidade"
    QRQC_FALHA = "QRQC_FALHA", "QRQC/Falha"
    PROCESSO_DESBLOQUEIO = "PROCESSO_DESBLOQUEIO", "Processo Desbloqueio"

class PalletInfo(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="pallets")
    serial_number = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    work_order = models.CharField(max_length=50, null=True, blank=True)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    customer_code = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_address = models.CharField(max_length=255, null=False, blank=False)
    stage = models.CharField(max_length=50, choices=Stage.choices)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_pallets")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReleasedPallet(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    first_box = models.IntegerField()
    last_box = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OnHoldPallet(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    hold_reason = models.CharField(max_length=100, choices=HoldReason.choices)
    observation = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RejectedPallet(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    issue = models.TextField()
    qrqc_failure = models.IntegerField(null=True, blank=True)
    step = models.CharField(max_length=100, choices=Step.choices)
    steps_completed = models.BooleanField()
    date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PalletSticker(models.Model):
    name = models.CharField(max_length=100, unique=True)
    encoding = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
    size = models.IntegerField()
    file_path = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
