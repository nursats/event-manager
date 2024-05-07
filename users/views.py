from django.shortcuts import render


def login(request):
    context ={
        'title': 'login'
    }
    return render(request, 'users/login.html',context)

def register(request):
    context ={
        'title': 'register'
    }
    return render(request, 'users/register.html',context)

def profile(request):
    context ={
        'title': 'profile'
    }
    return render(request, 'users/profile.html',context)

def logout(request):
    context ={
        'title': 'logout'
    }
    return render(request, 'users/logout.html',context)


