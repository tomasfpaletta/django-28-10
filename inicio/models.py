from django.db import models

class Vehiculo(models.Model):
   marca = models.CharField(max_length=30)
   description = models.CharField(max_length=250)
    
def __str__(self):
        return f'{self.marca} - {self.id}'



