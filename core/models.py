from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    honorarios = models.DecimalField(max_digits=7, decimal_places=2)  
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)



    def __str__(self):
        return self.name