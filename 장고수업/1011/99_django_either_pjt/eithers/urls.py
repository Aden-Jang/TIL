from django.urls import path
from . import views 

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path(
        '<int:question_pk>/comments/', 
        views.comments_create, 
        name='comments_create'
    ),
    path('random/', views.random, name='random'),
]