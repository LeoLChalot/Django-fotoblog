from django.shortcuts import redirect, render
from authentification.models import User
from django import forms
from authentification.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(
        request,
        'authentification/index.html'
    )

class LoginPage(View):
    template_name = 'authentification/login.html'
    def get(self, request):
        form = LoginForm()
        message = ''
        return render(
                request,
                self.template_name,
                context={'form':form, 'message':message}
            )
    def post(self, request):
        form = LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                django_login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                message = 'Identifiants invalides.'
        return render(
                request,
                self.template_name,
                context={'form':form, 'message':message}
            )


def login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                django_login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                message = 'Identifiants invalides.'
    return render(
        request,
        'authentification/login.html',
        context={'form':form, 'message':message}
    )

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        print (f'Les données sont : {request.POST}')
        form = SignupForm(request.POST)
        if form.is_valid():
            print (f'==== Form valide ====')
            user = form.save()
            print (f'User : {user}')
            django_login(request, user)
            return redirect('login')
    return render(
        request,
        'authentification/signup.html',
        context={'form': form})

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')