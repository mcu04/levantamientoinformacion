from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    creado= models.DateTimeField(auto_now_add=True)
    realizado= models.DateTimeField(null=True, blank=True)
    existe= models.BooleanField(default=False)
    importante= models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
        return self.titulo + '- por ' + self.user.username
    
    
