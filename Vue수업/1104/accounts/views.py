from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm
# Create your views here.


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated: # 유저가 이미 가입된 상태라면
        return redirect("movies:index") # movies:index

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("movies:index")
    else: # GET 방식
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated: # 유저가 이미 가입된 상태라면
        return redirect("movies:index") # movies:index
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or "movies:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "accounts/login.html", context)


@require_http_methods(["POST"])
def logout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            auth_logout(request)
    return redirect("movies:index")


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person
    }
    return render(request, "accounts/profile.html", context)

@require_http_methods(["POST"])
def follow(request, user_pk):
    User = get_user_model()
    if request.user.is_authenticated:
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')