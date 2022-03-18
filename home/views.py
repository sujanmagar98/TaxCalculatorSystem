from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # test home page will update later
    return HttpResponse("Home page")


def about(request):
    # test about page will update later
    return HttpResponse("About page")




