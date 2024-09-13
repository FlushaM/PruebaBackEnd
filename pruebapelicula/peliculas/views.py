from django.shortcuts import render

# Create your views here.

def renderIndex(request):
    return render(request, 'peliculas/index.html')

def renderPeliculas(request):
    datos = {
        "pelicula1":"ScaryMovie",
        "descripcion1":"Esta pelicula es de acción",
        "valoracion1":5,
        "img1":"peli1.png",

        "pelicula2":"Toy Story",
        "descripcion2":"Esta pelicula es de animación",
        "valoracion2":4,

        "pelicula3":"django",
        "descripcion3":"Esta pelicula es de accion",
        "valoracion3":9,


    }
    return render(request, 'peliculas/peliculas.html', datos)
