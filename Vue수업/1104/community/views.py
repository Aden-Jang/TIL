from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_safe

from .models import Review, Comment
from .forms import ReviewCreationForm, CommentCreationForm

# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    User = get_user_model()
    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewCreationForm()
    context = {
        'form': form
    }
    return render(request, 'community/create.html', context)


@require_http_methods(['GET'])
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentCreationForm()
    comments = review.comments.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'community/detail.html', context)


@require_http_methods(['POST'])
def comments_create(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')       

    
@require_http_methods(['POST'])
def like(request, review_pk):
    me = request.user
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=me.pk).exists():
            review.like_users.remove(me)
            cnt = len(review.like_users.all())
            is_liked = False
        else:
            review.like_users.add(me)
            cnt = len(review.like_users.all())
            is_liked = True
        context = {
            'is_liked': is_liked,
            'cnt': cnt
        }
        return JsonResponse(context)
    return redirect("accounts:login")



