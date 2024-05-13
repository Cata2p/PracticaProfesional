from django.shortcuts import render
# prospectos/views.py
from rest_framework import generics
from .models import Cliente, Estado, Etapa, Prospecto, Usuario
from .serializers import ClienteSerializer, ProspectoSerializer, EtapaSerializer, EstadoSerializer

class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = ClienteSerializer

class ClienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProspectoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer

class ProspectoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer

class EstadoRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EtapaRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

