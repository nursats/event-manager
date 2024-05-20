from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from events.models import Event

from users.forms import UserLoginForm





def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('events:home'))
    else:
        form = UserLoginForm()

    

    context = {
        'title': 'Home - Авторизация',
        'form':form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    
    context = {
        'title': 'Home - Регистрация',
        
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    
    context = {
        'title': 'Home - Кабинет',
    }
    return render(request, 'users/profile.html', context)




def logout(request):
    ...