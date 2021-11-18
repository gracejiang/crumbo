from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from main.models import FoodPlace

def home_view(request):
    return render(request, 'home.html' )

def explore_view(request):
    searchText = (request.POST['searchText'] if ('searchText' in request.POST) else "")
    filterUser = (request.POST['filterUser'] if ('filterUser' in request.POST) else "")

    if filterUser == "all" or filterUser == "":
        foodplaces = FoodPlace.objects.filter(name__contains=searchText).order_by('-created_on')
    else:
        user = User.objects.get(username=filterUser)
        foodplaces = FoodPlace.objects.filter(name__contains=searchText).filter(author=user).order_by('-created_on')

    return render(request, 'explore.html', { 'foodplaces' : foodplaces } )

def grac_view(request):
    return render(request, 'grac.html' )

def cxlu_view(request):
    return render(request, 'cxlu.html' )

# viewing a foodplace
def foodplace_view(request, id):
    foodplace = get_object_or_404(FoodPlace, id=id)
    return render(request, 'foodplace.html', { 'foodplace': foodplace })