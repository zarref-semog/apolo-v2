from .views import PalletInfoViewSet

routes = [
    # (prefixo, viewset, basename)
    ("pallets", PalletInfoViewSet, "pallets"),
]