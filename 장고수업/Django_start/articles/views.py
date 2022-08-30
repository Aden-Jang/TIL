import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('here')
    # return HttpResponse("<h1>hola</h1>")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'orange', 'banana']
    info = {'name': 'ADEN'}
    context = {
        'foods': foods,
        'info' : info
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['햄버거', '크림파스타', '소고기', '껍데기']
    pick = random.choice(foods)
    context = {
        'foods' : foods,
        'pick': pick
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {'data': data}
    return render(request, 'articles/catch.html', context)

def fake_google(request):
    return render(request, 'articles/fake-google.html')

def hello(request, name):
    context = {'name' : name}
    return render(request, 'articles/hello.html', context)