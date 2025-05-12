from django.contrib import admin

from .models import Project  # Importamos nuestros modelos para administrarlos en el paned de admministrador de Django

#Creamos una clase extendida para agregarle los campos de fecha
class ProyectAdmin(admin.ModelAdmin): 
    readonly_fields = ('created','updated')


# Register your models here.
admin.site.register(Project,ProyectAdmin) # Registramos nuestros modelos, y le pasasmos la sumbclase