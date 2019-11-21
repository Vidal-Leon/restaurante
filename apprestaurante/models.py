from django.db import models
from django.utils import timezone
from django.contrib import admin

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class MenuInLine(admin.TabularInline):
    model = Menu
    extra = 1

class Venta(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (MenuInLine,)

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class ClienteAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class MenuAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)
