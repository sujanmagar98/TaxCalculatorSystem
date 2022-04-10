from curses import use_default_colors
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile

from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created? You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    all_content = UserProfile.objects.filter(sel_user_id=request.user.id)
    ms =  UserProfile.objects.filter(sel_user_id=request.user.id).values('marital_status')
    
    


    s = []
    for x in all_content:
        s.append(x.marital_status)
    
    m_status = ' '.join([str(elem) for elem in s])
    # print(m_status)

    sal = []
    for p in all_content:
        sal.append(p.salary)


    a = ' '.join([str(elem) for elem in sal])
    taxable_income = float(a)
    # print(taxable_income)

    # logic for calculating tax
    tax = 0.0
    if m_status == "unmarried":
        if taxable_income <= 400000:
            tax = taxable_income * .01
        elif taxable_income <= 500000:
            tax = 4000 + .1 *(taxable_income - 400000)
        elif taxable_income <= 700000:
            tax = 14000 + .2 *(taxable_income - 500000)
        elif taxable_income <= 2000000:
            tax = 54000 + .3 *(taxable_income - 700000)
        else:
            tax = 444000 + .36 *(taxable_income - 1300000)
    elif m_status == "married":
        if taxable_income <= 450000:
            tax = taxable_income * .01
        elif taxable_income <= 550000:
            tax = 4500 + .1 *(taxable_income - 450000)
        elif taxable_income <= 750000:
            tax = 14500 + .2 *(taxable_income - 550000)
        elif taxable_income <= 2050000:
            tax = 54500 + .3 *(taxable_income - 750000)
        else:
            tax = 429500 + .36 *(taxable_income - 1300000)
    # print(tax)
  
    return render(request,'users/profile.html',{'all_content':all_content,'tax':tax})



# options
# message.debug
# message.info
# message.success
# message.warning
# message.error
