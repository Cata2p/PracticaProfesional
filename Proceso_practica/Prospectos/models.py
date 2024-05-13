from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    pass
    groups = models.ManyToManyField(Group, related_name='usuarios_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

class Prospecto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    sexo = models.CharField(max_length=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)

class Estado(models.Model):
    estado = models.CharField(max_length=50, choices=[('Abierto', 'Abierto'), ('Perdido', 'Perdido'), ('Ganado', 'Ganado')])

class Etapa(models.Model):
    etapa = models.CharField(max_length=50, choices=[('En conversación', 'En conversación'), ('Conseguido', 'Conseguido'), ('Perdido', 'Perdido')])

