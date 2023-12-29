from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/main-page.html')


def test_crator(request):
    return render(request, 'main/test-creator.html')


def library(request):
    return render(request, 'main/library.html')


def mastery(request):
    return render(request, 'main/mastery.html')


def test(request):
    return render(request, 'main/test-info.html')