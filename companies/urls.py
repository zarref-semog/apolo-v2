from .views import CompanyViewSet

routes = [
    # (prefixo, viewset, basename)
    ("companies", CompanyViewSet, "companies"),
]