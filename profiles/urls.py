from .views import UserViewSet, ProfileViewSet

routes = [
    # (prefixo, viewset, basename)
    ("users", UserViewSet, "users"),
    ("profiles", ProfileViewSet, "profiles"),
]