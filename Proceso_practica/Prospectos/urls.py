# prospectos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListCreateAPIView.as_view(), name='cliente-list-create'),
    path('prospectos/', views.ProspectoListCreateAPIView.as_view(), name='prospecto-list-create'),
    path('prospectos/<int:pk>/', views.ProspectoRetrieveUpdateDestroyAPIView.as_view(), name='prospecto-retrieve-update-destroy'),
]
