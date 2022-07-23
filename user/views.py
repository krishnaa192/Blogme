from concurrent.futures import process
from django.shortcuts import render
from .models import Profile

def authors(request):
    author=Profile.objects.all()
    a_pms={'author':author}
    return render(request, "author.html" , a_pms)