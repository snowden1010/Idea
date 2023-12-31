from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    product = Product.objects.first()
    return render(request, "Products/index.html", {"product":product})

def new(request):
    return HttpResponse("Woow the new worked")