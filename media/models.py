from django.db import models


# agregamos valores default para 
# que no tengamos que hacerlo 
# despues de hacer las migraciones:

class MediaContent(models.Model):
    link = models.URLField()  # Enlace al contenido aqui si no ponemos valor default porque cuando migramos ya estaba definido
    poster = models.URLField(default="https://via.placeholder.com/300")  # Póster del contenido
    title_image = models.URLField(default="https://via.placeholder.com/150x50")  # Imagen PNG del título
    transition_image = models.URLField(default="https://via.placeholder.com/150")  # Imagen PNG de transición

    def __str__(self):
        return self.link
