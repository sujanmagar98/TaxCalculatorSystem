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
        return HttpResponseRedirect("/closure")
    

    return render(request, 'home/contact.html')




def calculator(request):
    tax = 0.0
    try:
        if request.method=="POST":
            mStatus = request.POST.get('mStatus')
            fYear = request.POST.get('fiscalYear')
            income = float(request.POST.get('income')) 
            deduction = float(request.POST.get('deduction')) 
            taxable_income = income - deduction
            if mStatus == "unmarried" and fYear == "2020-21":
                if taxable_income <= 400000:
                    tax = taxable_income * .01
                elif taxable_income <= 500000:
                    tax = 4000 + .1 *(taxable_income - 400000)
                elif taxable_income <= 700000:
                    tax = 14000 + .2 *(taxable_income - 500000)
                elif taxable_income <= 1300000:
                    tax = 54000 + .3 *(taxable_income - 700000)
                else:
                    tax = 444000 + .36 *(taxable_income - 1300000)


            elif mStatus == "married" and fYear == "2020-21":
                if taxable_income <= 450000:
                    tax = taxable_income * .01
                elif taxable_income <= 550000:
                    tax = 4500 + .1 *(taxable_income - 450000)
                elif taxable_income <= 750000:
                    tax = 14500 + .2 *(taxable_income - 550000)
                elif taxable_income <= 1350000:
                    tax = 54500 + .3 *(taxable_income - 750000)
                else:
                    tax = 429500 + .36 *(taxable_income - 1300000)
            

            elif mStatus == "married" and fYear == "2018-19" :
                if taxable_income <= 400000:
                    tax = taxable_income * .01
                elif taxable_income <= 500000:
                    tax = 4000 + .1 *(taxable_income - 400000)
                elif taxable_income <= 700000:
                    tax = 14000 + .2 *(taxable_income - 500000)
                elif taxable_income <= 2000000:
                    tax = 54000 + .3 *(taxable_income - 700000)
                else:
                    tax = 444000 + .36 *(taxable_income - 2000000)

            
            if mStatus == "unmarried"and fYear == "2018-19":
                if taxable_income <= 350000:
                    tax = taxable_income * .01
                elif taxable_income <= 450000:
                    tax = 3500 + .1 *(taxable_income - 350000)
                elif taxable_income <= 650000:
                    tax = 13500 + .2 *(taxable_income - 450000)
                elif taxable_income <= 2000000:
                    tax = 53500 + .3 *(taxable_income - 650000)
                else:
                    tax = 458500 + .36 *(taxable_income - 2000000)


            request.session['tax'] = tax
            request.session['fYear'] = fYear
            request.session['mStatus'] = mStatus
            request.session['income'] = income
            request.session['taxable_income'] = taxable_income
            request.session['deduction'] = deduction

            return HttpResponseRedirect("/result")
    
    except:
        tax = "Invalid info"
        






    # try:
    #     if request.method=="POST":
    #         tax = 2.3
    #         mStatus = request.POST.get('mStatus')
    #         fYear = request.POST.get('fiscalYear')
    #         income = float(request.POST.get('income')) 
    #         deduction = float(request.POST.get('deduction')) 
    #         taxable_income = income - deduction


    #         if mStatus == "unmarried":
    #             if taxable_income <= 400000:
    #                 tax = taxable_income * .01
    #             elif taxable_income <= 500000:
    #                 tax = 4000 + .1 *(taxable_income - 400000)
    #             elif taxable_income <= 700000:
    #                 tax = 14000 + .2 *(taxable_income - 500000)
    #             elif taxable_income <= 2000000:
    #                 tax = 54000 + .3 *(taxable_income - 700000)
    #             else:
    #                 tax = 444000 + .36 *(taxable_income - 1300000)
    #         elif mStatus == "married":
    #             if taxable_income <= 450000:
    #                 tax = taxable_income * .01
    #             elif taxable_income <= 550000:
    #                 tax = 4500 + .1 *(taxable_income - 450000)
    #             elif taxable_income <= 750000:
    #                 tax = 14500 + .2 *(taxable_income - 550000)
    #             elif taxable_income <= 2050000:
    #                 tax = 54500 + .3 *(taxable_income - 750000)
    #             else:
    #                 tax = 429500 + .36 *(taxable_income - 1300000)
                
            
            

    # except:
    #     tax = "Invalid Info"

    

    return render(request, 'home/calculator.html',{'tax':tax})



def result(request):
    tax = request.session['tax']
    mStatus = request.session['mStatus']
    fYear = request.session['fYear']
    income = request.session['income']
    taxable_income = request.session['taxable_income']
    deduction = request.session['deduction']
    return render(request, 'home/result.html',{'mStatus':mStatus,'tax':tax,'fYear':fYear,'income':income,'taxable_income':taxable_income,'deduction':deduction})

def closure(request):


    return render(request, 'home/closure.html')

