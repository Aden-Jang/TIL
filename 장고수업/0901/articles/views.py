import random
from django.shortcuts import render

# Create your views here.
def index(request):
    print("here")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'orange', 'banana']
    info = {'name': 'AIDEN'}
    context = {
        'foods': foods,
        'info': info
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['초밥', '알리오올리오', '제로콜라']
    pick = random.choice(foods)
    context = {
        'foods': foods,
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
