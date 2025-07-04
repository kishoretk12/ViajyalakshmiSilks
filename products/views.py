from django.shortcuts import render
from .models import Saree

def home(request):
    items = Saree.objects.all()
    return render(request, 'home.html', {'items': items})
