from django.db import models
from django import forms

from datetime import datetime
from django.contrib.auth.models import User

from apply_app.models import Apply

# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_item = models.ManyToManyField(Apply, blank=True)    
