from django.db import models
from django.contrib.auth.models import User
from pallets.models import PalletInfo

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

class WipReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    pallet = models.ForeignKey(PalletInfo, on_delete=models.CASCADE)
    contains_label = models.BooleanField()
    pallet_condition = models.BooleanField()
    boxes_organization = models.BooleanField()
    batch_removal = models.DateTimeField()
    observation = models.TextField()
    correction = models.TextField()
    fraction = models.IntegerField(null=True, blank=True)
    amount_default = models.IntegerField(null=True, blank=True)
    images = models.JSONField(default=list, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report {self.pallet.serial_number}"

class ReleasedPalletReport(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    first_box = models.IntegerField()
    last_box = models.IntegerField()
    images = models.JSONField(default=list, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Released: {self.pallet.serial_number}"

class OnHoldPalletReport(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    hold_reason = models.CharField(max_length=100, choices=HoldReason.choices)
    observation = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    images = models.JSONField(default=list, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"On Hold: {self.pallet.serial_number}"

class RejectedPalletReport(models.Model):
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    pallet = models.OneToOneField(PalletInfo, on_delete=models.CASCADE)
    issue = models.TextField()
    qrqc_failure = models.IntegerField(null=True, blank=True)
    step = models.CharField(max_length=100, choices=Step.choices)
    steps_completed = models.BooleanField()
    date = models.DateTimeField(null=True, blank=True)
    images = models.JSONField(default=list, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rejected: {self.pallet.serial_number}"
