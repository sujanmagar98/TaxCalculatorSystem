from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Tax_info(models.Model): 
    # define different fields/columns for package
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True,max_length=50, unique=True)
    image = models.ImageField(null=True,blank=True,upload_to = "images/")
    content = RichTextField(blank=True)
    # content = models.TextField()

    def __str__(self):
        return self.title




class  Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True,max_length=50, unique=True)
    intro = models.TextField(null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title


        
# get review from the user
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    # to know the date, the review has been given
    date = models.DateTimeField(auto_now_add=True, blank=True)
    comments = models.TextField(max_length=900,null=True)

    def __str__(self):
        return 'Message from '+ self.fname







