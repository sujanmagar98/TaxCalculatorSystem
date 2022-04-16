from http.client import HTTPResponse
from django.shortcuts import render
from .models import Tax_info

# Create your views here.
# def index(request):
#     # test home page will update later
#     return render(request, 'home/index.html')


def index(request):                                                        
    tax_info = Tax_info.objects.all()
    return render(request, "home/index.html", {"tax_info":tax_info})

def about(request):
    # test about page will update later
    return render(request, 'home/about.html')


