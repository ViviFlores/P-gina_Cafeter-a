from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    return render(request, "blog/blog.html", {'blogs': blogs})


def category(request, categoryId):
    #category = Category.objects.get(id=categoryId)
    category = get_object_or_404(Category, id=categoryId)  # un registro
    # filtrar las entradas de acuerdo a la categoria
    blogs = Blog.objects.filter(categories=category)
    return render(request, "blog/category.html", {"blogs": blogs})
