from django import forms
from django.contrib.auth import get_user_model
from .models import Review, Comment

class ReviewCreationForm(forms.ModelForm):

    class Meta:
        model=Review
        fields="__all__"
        exclude=('user', 'like_users')

class CommentCreationForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields="__all__"
        exclude=('user', 'review', 'like_users')