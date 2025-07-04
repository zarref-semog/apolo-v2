from .views import ReportViewSet

routes = [
    # (prefixo, viewset, basename)
    ("reports", ReportViewSet, "reports")
]