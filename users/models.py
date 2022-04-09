from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


# Create your models here.

class UserProfile(models.Model):
    sel_user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    marital_status = models.TextField(max_length=200, null= True, blank=True)
    salary = models.TextField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.sel_user.username



