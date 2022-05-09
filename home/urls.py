from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path("contact", views.contact, name = "contact"),
    path('about', views.about, name='about'),
    path('<slug:slug>', views.tax_detail, name='tax_detail'), 
    path("blog/", views.blog, name = "blog"),
    path('blog/<slug:slug>/', views.post_detail, name= "post_detail"),


]
