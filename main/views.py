from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html' )

def explore_view(request):
    return render(request, 'explore.html' )