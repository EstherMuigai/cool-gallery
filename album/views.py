from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    categories = Category.objects.all()
    return render(request, 'landingpage.html',{"categories":categories})

def categories(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'categories.html',{"categories":categories,"images":images})

def category(request):
    images = Image.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'category.html',{"message":message,"category": searched_category,"images":images})

    else:
        message = "Invalid."
        return render(request, 'landingpage.html',{"message":message})

def location(request):
    return render(request, 'location.html')


