from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def trending(request):
    return render(request, 'trending.html')