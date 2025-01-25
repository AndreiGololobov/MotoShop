from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    #categories = Categories.objects.all()
    
    context= {
        'title': 'BikeShop',
        'content': 'Welcome to BIKE SHOP',
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context={
        'title': 'About Page',
        'content': 'This Page about our Company',
        'text_on_page': 'Наши мотоциклы самые лучшие',
    }
    return render(request, 'main/about.html',context)

def contacts(request):
    return HttpResponse('Contact Page')