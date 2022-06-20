from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # Profile.get_or_create(user=request.user)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for { username }!!')
            return redirect('home')

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)