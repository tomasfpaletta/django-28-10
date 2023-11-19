from django.db import models


class Vehiculo(models.Model):
    tipo = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    fecha_creacion = models.DateField()
    
    def __str__(self): 
        return f'{self.tipo} - {self.modelo}'
    
class SUVs(Vehiculo):
    numero_puertas = models.IntegerField()
    
    def __str__(self):
        return f"SUVs {super().__str__()} - Puertas: {self.numero_puertas}"

class Camioneta(Vehiculo):
    capacidad_carga = models.FloatField()

    def __str__(self):
        return f"Camioneta {super().__str__()} - Capacidad de carga: {self.capacidad_carga} toneladas"
    
    
class Auto(Vehiculo):
    numero_puertas = models.IntegerField()
    
    def __str__(self):
        return f"Auto {super().__str__()} - Puertas: {self.numero_puertas}"
