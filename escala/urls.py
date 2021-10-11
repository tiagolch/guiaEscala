from django.urls import path, include
from .views import MinhaEscalaView, EscalaView

urlpatterns = [
    path('', MinhaEscalaView, name='minhaescala'),
    path('escala', EscalaView, name='escala'),
]
