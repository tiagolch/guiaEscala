from django.urls import path, include
from .views import MinhaEscalaView

urlpatterns = [
    path('minhaescala/', MinhaEscalaView, name='minhaescala'),
]
