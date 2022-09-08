from socket import fromshare
from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목'
    )
    content = forms.CharField(
        label='내용'
    )
    
    class Meta:
        model = Article
        fields = '__all__'
