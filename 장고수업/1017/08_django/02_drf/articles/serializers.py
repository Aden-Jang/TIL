from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 기사의 댓글 pk값만 확인 가능
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # CommentSerializer를 위로 보내고 아래 코드를 작성하면 기사의 댓글 상세정보까지 볼 수 있음
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



