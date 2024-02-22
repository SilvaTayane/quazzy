import os
from django.shortcuts import render
from django.conf import settings
from .models import Publication
from PIL import Image

def home(request):
    if request.method =="POST":
        publi = Publication()
        publi.nome = request.POST.get("nome") 
        publi.text = request.POST.get("text")
        publi.arq = request.FILES.get("my_file")
        
        publi.save()
        
        conteudo = {
            'conteudo':Publication.objects.all()[::-1]
        }

        return render(request,'index.html',conteudo)

    else:
        conteudo = {
            'conteudo':Publication.objects.all()[::-1]
        }

        return render(request,'index.html',conteudo)
        

def profile(request):
    if request.method =="POST":
        publi = Publication()
        publi.nome = request.POST.get("nome") 
        publi.text = request.POST.get("text")
        publi.arq = request.FILES.get("my_file")
        
        publi.save()
        
        conteudo = {
            'conteudo':Publication.objects.all()[::-1]
        }

        return render(request,'profile.html',conteudo)

    else:
        conteudo = {
            'conteudo':Publication.objects.all()[::-1]
        }

        return render(request,'profile.html',conteudo)

def trending(request):
    return render(request, 'trending.html')