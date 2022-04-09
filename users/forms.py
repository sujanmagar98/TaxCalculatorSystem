from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import  UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class']= 'form-control'
        self.fields['last_name'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'