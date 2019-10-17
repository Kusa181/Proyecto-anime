from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    TipoGenero = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Anim (models.Model):
    Nombre = models.CharField(max_length=200)
    Creador = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    Descripcion = models.TextField(max_length=1000, help_text='introdusca una breve descripcion del Anime')
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.Nombre
    
    def get_absolute_url(self):
        return reverse ('anim-detail', args=[str(self.id)])

class AnimInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Id para el el anime en particular con los demas' )
    anim = models.ForeignKey('Anim', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} ({self.anim.Nombre})'

class Author(models.Model):
    Primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Nacimiento = models.DateField( null=True, blank=True)

    class Meta:
        ordering = ['apellido','Primer_nombre']
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.apellido}, {self.Primer_nombre}'