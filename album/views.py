from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'landingpage.html')

def categories(request):
    return render(request, 'categories.html')

def category(request,categoryname):
    return render(request, 'category.html')

def location(request):
    return render(request, 'location.html')


