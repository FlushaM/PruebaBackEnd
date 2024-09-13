from django.shortcuts import render

# Create your views here.

def renderIndex(request):
    return render(request, 'peliculas/index.html')

def renderTiburon(request):
    datos = {
        "pelicula1":"Tiburon",
        "descripcion1":"Esta pelicula es de acción",
        "valoracion1":5,
        "img1":"peli1.png",


    }
    return render(request, 'peliculas/peliculas.html', datos)

def renderScaryMovie(request):
    datos = {
        "pelicula1":"ScaryMovie",
        "descripcion1":"Esta pelicula es de acción",
        "valoracion1":5,
        "img1":"peli1.png",



    }
    return render(request, 'peliculas/peliculas.html', datos)

def renderJango(request):
    datos = {

        "pelicula1":"django",
        "descripcion1":"Esta pelicula es de accion",
        "valoracion1":9,
        "img1":"peli3.png",



    }
    return render(request, 'peliculas/peliculas.html', datos)
