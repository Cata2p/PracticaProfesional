

from rest_framework import serializers
from .models import Usuario, Cliente, Prospecto, Estado, Etapa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'estado']

class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = ['id', 'etapa']

class ProspectoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
    etapa = EtapaSerializer()

    cliente_rut = serializers.CharField(source='cliente.rut', read_only=True)  # Accedemos al rut del cliente

    class Meta:
        model = Prospecto
        fields = ['nombre', 'email', 'telefono', 'fecha_ingreso', 'sexo', 'cliente', 'cliente_rut', 'estado', 'etapa']

    def create(self, validated_data):
        estado_data = validated_data.pop('estado')
        etapa_data = validated_data.pop('etapa')

        estado = Estado.objects.create(**estado_data)
        etapa = Etapa.objects.create(**etapa_data)

        prospecto = Prospecto.objects.create(estado=estado, etapa=etapa, **validated_data)
        return prospecto