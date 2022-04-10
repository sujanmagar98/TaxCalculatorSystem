from http.client import HTTPResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    # test home page will update later
    return render(request, 'home/index.html')


def about(request):
    # test about page will update later
    return render(request, 'home/about.html')


