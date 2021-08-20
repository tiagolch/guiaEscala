from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escala.views import EscalaViewSet, EventoViewSet


router = routers.DefaultRouter()
router.register(r'escala', EscalaViewSet)
router.register(r'evento', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]