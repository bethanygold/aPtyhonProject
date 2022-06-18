from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(max_length=50)
    Published_date = models.DateTimeField(max_length=50)
