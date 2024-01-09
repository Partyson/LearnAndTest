from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Questions
from .models import Tests
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'main/main-page.html')


def test_creator(request):
    return render(request, 'main/test-creator.html')


def library(request):
    return render(request, 'main/library.html')


def mastery(request):
    return render(request, 'main/mastery.html')


def test(request):
    return render(request, 'main/test-info.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login(request):
   if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse('index'))
   else:
       form = AuthenticationForm()
   return render(request, 'login.html', {'form': form})
