from .views import PalletInfoViewSet

routes = [
    # (prefixo, viewset, basename)
    ("pallets", PalletInfoViewSet, "pallets"),
    ("released-pallets", PalletInfoViewSet, "released-pallets"),
    ("on-hold-pallets", PalletInfoViewSet, "on-hold-pallets"),
    ("rejected-pallets", PalletInfoViewSet, "rejected-pallets"),
]