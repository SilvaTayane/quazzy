import os
from django.shortcuts import render
from django.conf import settings
from .models import Publication
from PIL import Image

def home(request):
    if request.method =="POST":
        file = request.FILES.get("my_file")
        
        img = Image.open(file)  
        path = os.path.join(settings.BASE_DIR,f'a.png')      
        
        img = img.save(path)
        
        return render(request,'index.html')

    else:
        return render(request, 'index.html')
        

def profile(request):
    return render(request, 'profile.html')

def trending(request):
    return render(request, 'trending.html')