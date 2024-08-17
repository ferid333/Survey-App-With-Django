from ssl import Options
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
# Create your models here.
class Survey(models.Model):
    question=models.TextField()
    user=models.CharField(max_length=2000)
    datetime=models.DateTimeField(default=datetime.now,blank=True)
    option1=models.CharField(max_length=2000,null=True,blank=True)
    option2=models.CharField(max_length=2000,null=True,blank=True)
    option3=models.CharField(max_length=2000,null=True,blank=True)
    option4=models.CharField(max_length=2000,null=True,blank=True)
    option5=models.CharField(max_length=2000,null=True,blank=True)
    option1_count=models.IntegerField(null=True,blank=True,default=0)
    option2_count=models.IntegerField(null=True,blank=True,default=0)
    option3_count=models.IntegerField(null=True,blank=True,default=0)
    option4_count=models.IntegerField(null=True,blank=True,default=0)
    option5_count=models.IntegerField(null=True,blank=True,default=0)
    slug=models.SlugField(blank=True,null=False,unique=True)
    allcounts=models.IntegerField(null=True,blank=True,default=1)
    def save(self,*args, **kwargs):
        self.slug=slugify(self.question)
        self.allcounts=self.option1_count+self.option2_count+self.option3_count+self.option4_count+self.option5_count
        super().save(*args, **kwargs)