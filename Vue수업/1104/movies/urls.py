from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('recommended/', views.recommended, name='recommended'),
    path('<int:movie_pk>/', views.detail, name='detail'),
]