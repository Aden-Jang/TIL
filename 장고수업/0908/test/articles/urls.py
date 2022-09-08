from django.urls import path
from articles import views

app_name='articles'
urlpatterns = [
    path('', views.index, name="index")
]
