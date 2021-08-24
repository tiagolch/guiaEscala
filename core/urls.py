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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]