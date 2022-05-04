from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tax_info(models.Model): 
    # define different fields/columns for package
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True,max_length=50, unique=True)
    image = models.ImageField(null=True,blank=True,upload_to = "images/")
    content = models.TextField()

    def __str__(self):
        return self.title








