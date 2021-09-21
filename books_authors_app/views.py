from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    if request.method == "GET":
        print("a GET request is being made to this route")

        context = {
            'saludo': 'Hola',
            'all_libros' : Book.objects.all()
        }
        return render(request, 'index.html', context)

    if request.method == "POST":
        print("a POST request is being made to this route")
        print(request.POST)
        print(request.POST["titulo"])
        print(request.POST["dsc"])
        titulo=request.POST["titulo"]
        dsc=request.POST["dsc"]
        Book.objects.create(title=titulo,desc=dsc)
        return redirect("/")


def autor(request):
    if request.method == "GET":
        print("a GET request is being made to this route")

        context = {
            'all_autores' : Author.objects.all()
        }
        return render(request, 'autores.html', context)

    if request.method == "POST":
        print("a POST request is being made to this route")
        print(request.POST)
        print(request.POST["nombre"])
        print(request.POST["apellido"])
        print(request.POST["notas"])

        nombre =request.POST["nombre"]
        apellido =request.POST["apellido"]
        notas =request.POST["notas"]
        Author.objects.create(first_name=nombre, last_name=apellido, notas=notas)
        return redirect("/autores")


def libros(request, my_val):

    if request.method == "GET":
        print("a GET request is being made to this route")
        libro=Book.objects.get(id=my_val)
        autores = libro.authors.all()

        context = {
            'all_authors' : Author.objects.all(),
            'all_libros' : Book.objects.all(),
            'libro' : libro,
            'autores' : autores
        }
        print(autores)
        return render(request, 'libros.html', context)

    if request.method == "POST":
        print("a POST request is being made to this route")
        print(request.POST)
    #no se como redirigir aqui
        return redirect("")


    context = {
        'saludo': 'Hola' 
    }
    return render(request, 'libros.html', context)


