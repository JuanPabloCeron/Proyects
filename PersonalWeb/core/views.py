#para desactovar plynt:
# pylint: skip-file

from django.shortcuts import render,HttpResponse

#Variable multilinea para ella estructura de un  html:
#Cada uno de los <li> hace referencia a una de las vistas que hemos creado en urls.py

#*****************************************************************
def home(request):
  
  return render(request,"core/home.html") # devolvemos un render con la resquests seguida del directorio de nuestro html
#*****************************************************************

def about(request):
    
    return render(request,"core/about_me.html")

#*****************************************************************

def contact(request):

    return render(request,"core/contact.html")