from django.urls import path
from .views import Aventura, index

urlpatterns = [
    path('', index, name='index'),
    path('', Aventura, name='Aventura')
]