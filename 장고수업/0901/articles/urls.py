from django.urls import path
from articles import views

app_name = "articles"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('greeting/', views.greeting, name="greeting"),
    path('dinner/', views.dinner, name="dinner"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('fake-google/', views.fake_google, name="fake-google"),
    path('hello/<str:name>/', views.hello, name="hello"),
]
