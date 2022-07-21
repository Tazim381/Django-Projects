from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all() #Book er object gula books e rakhtesi
    return render(request,'mylabbook/home.html',{'books':books})  #reutn templates->mylabbook er home page ,{}->touple

