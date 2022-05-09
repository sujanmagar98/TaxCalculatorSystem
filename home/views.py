from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact, Tax_info
from .models import Post
from .models import Contact

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

def blog(request):
    posts = Post.objects.all()
    return render(request, "home/blog.html", {"posts":posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "home/post_detail.html", {'post':post})



def tax_detail(request,slug):
    tax_info = Tax_info.objects.get(slug=slug) 
    return render(request, "home/taxdetail.html",{"tax_info":tax_info})




def contact(request):
    if request.method=="POST":
        # Object for Contact
        contact = Contact()
        # getting info from user
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        # save in form model
        contact.fname= fname
        contact.lname= lname
        contact.email = email
        contact.phone = phone
        contact.comments = comments
        contact.save()
    return render(request, 'home/contact.html')



