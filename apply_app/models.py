from django.db import models

# Create your models here.

class Apply(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    major=models.CharField(max_length=20)
    url=models.CharField(max_length=20)
    why = models.TextField()
    service = models.TextField()
    memory = models.TextField()
    coding = models.TextField()
    
    def __str__(self):
        return self.name