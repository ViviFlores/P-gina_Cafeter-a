from django.shortcuts import render


# Create your views here.


def home(request):  # request -> petición desde el navegador
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def store(request):
    return render(request, "core/store.html")
