from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'pages/home.html')


def information(request):
    return render(request, 'pages/information.html')


def contact(request):
    return render(request, 'pages/contact.html')


def news(request):
    return render(request, 'pages/news.html')


def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})
