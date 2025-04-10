from django.db import models

class Palabra(models.Model):
    NIVELES = (
        ('F', 'Fácil'),
        ('M', 'Medio'),
        ('D', 'Difícil'),
    )
    
    palabra = models.CharField(max_length=50)
    nivel = models.CharField(max_length=1, choices=NIVELES)
    imagen = models.ImageField(upload_to='imagenes/')
    audio = models.FileField(upload_to='audios/')
    
    def __str__(self):
        return self.palabra