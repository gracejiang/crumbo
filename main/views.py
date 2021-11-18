from django.shortcuts import render, get_object_or_404
from main.models import FoodPlace

def home_view(request):
    return render(request, 'home.html' )

def explore_view(request):
    
    foodplaces = FoodPlace.objects.order_by('-created_on')
    return render(request, 'explore.html', { 'foodplaces' : foodplaces } )

def grac_view(request):
    return render(request, 'grac.html' )

def cxlu_view(request):
    return render(request, 'cxlu.html' )

# viewing a foodplace
def foodplace_view(request, id):
    foodplace = get_object_or_404(FoodPlace, id=id)
    return render(request, 'foodplace.html', { 'foodplace': foodplace })