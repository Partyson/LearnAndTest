from django.shortcuts import render

def index(request):
    return render(request, 'test_creator/web2.html')
