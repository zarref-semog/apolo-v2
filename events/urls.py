from .views import EventViewSet

routes = [
    # (prefixo, viewset, basename)
    ("events", EventViewSet, "events"),
]