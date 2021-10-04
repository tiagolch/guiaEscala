from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escala.views import EscalaViewSet, EventoViewSet
from ministerio.views import MinisterioViewSet, FuncaoViewSet


router = routers.DefaultRouter()
router.register(r'escala', EscalaViewSet, basename='Escala')
router.register(r'evento', EventoViewSet, basename='Evento')
router.register(r'ministerio', MinisterioViewSet, basename='Ministerio')
router.register(r'funcao', FuncaoViewSet, basename='Funcao')

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('escala/', include('escala.urls')),
    path('api/', include(router.urls)),
]