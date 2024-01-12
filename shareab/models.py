from django.db import models
from django.contrib.auth.models import User
from .choices import CAMPUS_CHOICES
from django.core.validators import MaxLengthValidator

# Create your models here.

class Profile(models.Model):
    campus = models.CharField(max_length=10, choices=CAMPUS_CHOICES)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(upload_to='profile_picture/',null=True,blank=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    content  = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

