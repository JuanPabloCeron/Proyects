from django.db import models

# Create your models here.

#------------------------------------------------------------------------------------------------------
class Project(models.Model): #Esta super clase models.Model representa una clase como una tabal en la db

    title = models.CharField(max_length=200, verbose_name="Titulo") # Con ChadField hacemos que esa variable sea de tipo char, asi nuestro ORM lo guarda en la base de datos
    description = models.TextField(verbose_name="Descripción") # Cuando los textos son mas grande usamos Texfield
    image = models.ImageField(verbose_name="Imagen",upload_to="projects") #De esta manera le indicamos que las imagenes se guarden en el directorio /media/projects
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #Se ejecuta solo la primera vez que se crea la instancia
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición") #Se ejecuta cada vez que se actualiza una instancia

#------------------------------------------------------------------------------------------------------   
    
    # Creamos una subclase con metadatos 
    class Meta: 
        
        verbose_name= "proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"] # Campo de ordancion por defecto para nuestros registros, en este caso con "-created" ordenamos de mas nuevos a mas antiguos, si fuera al contrario basta solo "created"
        
#-------------------------------------------------------------------------------------------------------        
    #Con esta funcion String le indicamos que devuelva el nombre de la clase
    def __str__(self):
        return f"{self.title}"