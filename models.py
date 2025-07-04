from django.db import models

class Role(models.TextChoices):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    MANAGEMENT = "MANAGEMENT"
    WAREHOUSE = "WAREHOUSE"

class ReportStatus(models.TextChoices):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"

class StageType(models.TextChoices):
    PACKAGING = "PACKAGING"
    WIP = "WIP"
    STORAGE = "STORAGE"
    PRODUCTION_FOR_REVIEW = "PRODUCTION_FOR_REVIEW"
    PACKAGING_FOR_REVIEW = "PACKAGING_FOR_REVIEW"
    WIP_FOR_REVIEW = "WIP_FOR_REVIEW"
    FINISHED = "FINISHED"

class DeviceStatus(models.TextChoices):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

class QualityPalletStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class HoldReason(models.TextChoices):
    AGUARDANDO_AGIN_DAT = "AGUARDANDO_AGIN_DAT"
    AGUARDANDO_OP = "AGUARDANDO_OP"
    AGUARDANDO_DESVIO_ENGENHARIA = "AGUARDANDO_DESVIO_ENGENHARIA"
    AGUARDANDO_RESULTADO_ORT = "AGUARDANDO_RESULTADO_ORT"
    OUTROS = "OUTROS"

class Step(models.TextChoices):
    REVISAO_PRODUCAO = "REVISAO_PRODUCAO"
    REINSPECAO_QUALIDADE = "REINSPECAO_QUALIDADE"
    QRQC_OU_FALHA = "QRQC_OU_FALHA"
    PROCESSO_DESBLOQUEIO = "PROCESSO_DESBLOQUEIO"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Role.choices)
    registry = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

class Sector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True, related_name="sectors")
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True, related_name="sector_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Line(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="lines")
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True, related_name="line_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Turn(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_at = models.CharField(max_length=20)
    end_at = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True, related_name="turns")
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True, related_name="turn_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Company(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="companies")
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    cep = models.CharField(max_length=50)
    observation = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Country(models.Model):
    acronym = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class State(models.Model):
    acronym = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="states")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    acronym = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    state = models.ForeignKey("State", on_delete=models.CASCADE, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stage(models.Model):
    name = models.CharField(max_length=50, choices=StageType.choices, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pallet(models.Model):
    variant = models.CharField(max_length=100)
    batch = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    line = models.ForeignKey("Line", on_delete=models.CASCADE, related_name="pallets")
    current_stage = models.CharField(max_length=50, choices=StageType.choices)
    sticker = models.OneToOneField("PalletSticker", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PalletSticker(models.Model):
    name = models.CharField(max_length=100, unique=True)
    encoding = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
    size = models.IntegerField()
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PalletStage(models.Model):
    approval = models.BooleanField(null=True, blank=True)
    pallet = models.ForeignKey("Pallet", on_delete=models.CASCADE, related_name="stages")
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE, related_name="pallets")
    create_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["pallet", "stage"])]

class Report(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="reports")
    pallet_stage = models.ForeignKey("PalletStage", on_delete=models.CASCADE, related_name="report")
    turn = models.ForeignKey("Turn", on_delete=models.CASCADE)
    fraction = models.IntegerField(null=True, blank=True)
    amount_default = models.IntegerField(null=True, blank=True)
    quality_sheet = models.OneToOneField("QualitySheet", on_delete=models.SET_NULL, null=True, blank=True)
    time_batch_removal = models.IntegerField(null=True, blank=True)
    datime_batch_removal = models.DateTimeField(null=True, blank=True)
    cmes_image = models.TextField(null=True, blank=True)
    quality_sheet_image = models.TextField(null=True, blank=True)
    sap_registry = models.TextField(null=True, blank=True)
    description_compliant = models.TextField(null=True, blank=True)
    is_compliant = models.BooleanField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=ReportStatus.choices, null=True, blank=True)
    sloc = models.ForeignKey("SlocT", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QualitySheet(models.Model):
    report = models.OneToOneField("Report", on_delete=models.CASCADE, related_name="quality_sheet")
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SlocT(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True, related_name="slocs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PalletChangeHistory(models.Model):
    pallet = models.ForeignKey("Pallet", on_delete=models.CASCADE)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    report = models.ForeignKey("Report", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    changes = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class Inspection(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReportInspection(models.Model):
    report = models.ForeignKey("Report", on_delete=models.CASCADE)
    inspection = models.ForeignKey("Inspection", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    approval = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PalletImage(models.Model):
    report = models.ForeignKey("Report", on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)

class Batch(models.Model):
    quantity = models.IntegerField()
    weight = models.FloatField()
    invoice = models.OneToOneField("Invoice", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Invoice(models.Model):
    identifier = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255, unique=True)
    state_registration = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    value = models.FloatField()
    purchase_order = models.CharField(max_length=255, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    batch = models.OneToOneField("Batch", on_delete=models.SET_NULL, null=True, blank=True, related_name="invoice_ref")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InvoiceReport(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Inconsistency(models.Model):
    field = models.CharField(max_length=255)
    expected = models.FloatField()
    received = models.FloatField()
    invoice_report = models.ForeignKey("InvoiceReport", on_delete=models.CASCADE)

class BatchInspection(models.Model):
    batch = models.ForeignKey("Batch", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    is_approved = models.BooleanField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class InspectionImage(models.Model):
    inspection = models.ForeignKey("BatchInspection", on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)

class Device(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    reference = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=DeviceStatus.choices)
    last_sample = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bin(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    device = models.ForeignKey("Device", on_delete=models.CASCADE)
    capacity = models.FloatField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BinImage(models.Model):
    bin = models.ForeignKey("Bin", on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReleasedPallet(models.Model):
    inspector = models.ForeignKey("User", on_delete=models.CASCADE)
    pallet = models.ForeignKey("Pallet", on_delete=models.CASCADE)
    turn = models.ForeignKey("Turn", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=QualityPalletStatus.choices)
    first_box = models.IntegerField()
    last_box = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OnHoldPallet(models.Model):
    inspector = models.ForeignKey("User", on_delete=models.CASCADE)
    pallet = models.ForeignKey("Pallet", on_delete=models.CASCADE)
    turn = models.ForeignKey("Turn", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=QualityPalletStatus.choices)
    hold_reason = models.CharField(max_length=100, choices=HoldReason.choices)
    observation = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LockedPallet(models.Model):
    inspector = models.ForeignKey("User", on_delete=models.CASCADE)
    pallet = models.ForeignKey("Pallet", on_delete=models.CASCADE)
    issue = models.TextField()
    qrqc_failure = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=QualityPalletStatus.choices)
    step = models.CharField(max_length=100, choices=Step.choices)
    steps_completed = models.BooleanField()
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)