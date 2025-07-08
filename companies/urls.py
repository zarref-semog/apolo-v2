from .views import CompanyViewSet, ProductionLineViewSet

routes = [
    # (prefixo, viewset, basename)
    ("companies", CompanyViewSet, "companies"),
    ("production-lines", ProductionLineViewSet, "production-lines")
]