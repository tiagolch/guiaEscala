from django.urls import path, include
from .views import MinhaEscalaView

urlpatterns = [
    path('', MinhaEscalaView, name='minhaescala'),
]
