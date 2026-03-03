from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    imagen = models.ImageField(upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)
    recomendado = models.BooleanField(default=False)

    def str(self):
        return self.titulo

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    masajes = models.TextField()
    servicios = models.TextField()
    para_aprender = models.TextField(blank=True, null=True)
    acompanamiento_terapeutico = models.TextField(blank=True, null=True)
    horario_atencion = models.TextField()
    idiomas = models.TextField()
    imagen = models.ImageField(upload_to="staff/")
    activo = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs) 
    
    def __str__(self):
        return self.nombre
    