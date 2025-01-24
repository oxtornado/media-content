from django.db import models

# Create your models here.
class MediaContent(models.Model):
    link = models.URLField()  # Enlace al contenido
    poster = models.URLField()  # Póster del contenido
    title_image = models.URLField()  # Imagen PNG del título
    transition_image = models.URLField()  # Imagen PNG de transición

    def __str__(self):
        return self.link  # Representación textual del modelo
