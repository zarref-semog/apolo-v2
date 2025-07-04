"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

# Rotas das aplicações
from profiles.urls import routes as profile_routes
from companies.urls import routes as company_routes
from pallets.urls import routes as pallet_routes
from reports.urls import routes as report_routes
from events.urls import routes as event_routes

# Combina as rotas de todas as apps
routes = (
    profile_routes
    + company_routes
    + pallet_routes
    + report_routes
    + event_routes
)

router = DefaultRouter()

# Registra automaticamente os viewsets
for prefix, viewset, basename in routes:
    router.register(prefix, viewset, basename=basename)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    
    # Rotas de autenticação JWT
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
