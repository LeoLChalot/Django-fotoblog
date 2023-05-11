from django.shortcuts import redirect, render
from authentification.models import User
from django import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(
        request,
        'blog/home.html'
        )