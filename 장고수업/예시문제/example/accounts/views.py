from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:success')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def success(request):
    return render(request, 'accounts/success.html')