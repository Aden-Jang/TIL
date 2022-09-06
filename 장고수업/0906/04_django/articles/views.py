from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST

# Create your views here.
# GET 방식만 받는다
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# POST일 때만 데이터베이스를 조작하고 나머지는 큰 의미없는 것이므로 
# if request.method == 'POST':를 사용
# else가 GET일 때 가 아니라 POST가 아닐 때 이므로
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        # 유효성 검사(검증) 통과하면 True, 불통이면 False 반환
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)



    # form = ArticleForm(request.POST)
    # # 유효성 검사(검증) 통과하면 True, 불통이면 False 반환
    # if form.is_valid():
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    # # return redirect('articles:new')
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/new.html', context)
    
    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # if request.method == 'POST':
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # # form = ArticleForm(data=request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/deit.html', context)

    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)