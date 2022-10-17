from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def hello(request):
    data = {'username': 'aden'}
    return JsonResponse(data)