from .views import WipReportViewSet, ReleasedPalletReportViewSet, OnHoldPalletReportViewSet, RejectedPalletReportViewSet

routes = [
    # (prefixo, viewset, basename)
    ("wip-reports", WipReportViewSet, "wip-reports"),
    ("released-pallets-reports", ReleasedPalletReportViewSet, "released-pallets-reports"),
    ("on-hold-pallets-reports", OnHoldPalletReportViewSet, "on-hold-pallets-reports"),
    ("rejected-pallets-reports", RejectedPalletReportViewSet, "rejected-pallets-reports"),
]