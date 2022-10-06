from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user',)

class CommentFrom(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)
