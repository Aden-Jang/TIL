from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()
#     return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:    
        article = Article.objects.get(pk=article_pk)

        # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
        # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
        # if request.user in article.like_users.all():
        
        # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인
        if article.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소 (remove)
            article.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')