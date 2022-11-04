from django import forms
from django.contrib.auth import get_user_model
from .models import Movie, Genre

class MovieCreationForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('genres',)
