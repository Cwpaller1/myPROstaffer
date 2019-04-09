from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
        }
    return render(request, 'users/register.html', context)


def login(request):
    return render(request, 'users/login.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
