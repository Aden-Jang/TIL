from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

# Q 1.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
        
    # Q 2.
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)