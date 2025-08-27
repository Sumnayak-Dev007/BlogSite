from django.db import models
from django.contrib.auth.models import User
import datetime,os
# Create your models here.


def get_image_path(instance, filename):  # `request` → `instance`
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # Removed `:`
    filename = f"{nowTime}_{original_filename}"
    return f"images/{filename}"  # Removed `os.path.join()`


def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('category/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    descriptions=models.TextField(max_length= 500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Trending")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)
    
class Catblog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    title=models.CharField(max_length=150,null=False,blank=False)
    blog_image=models.ImageField(upload_to=get_image_path,null=True,blank=True)
    small_description=models.CharField(max_length= 250,null=False,blank=False)
    descriptions=models.TextField(max_length= 500,null=False,blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False,help_text="0=default,1=Trending")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return str(self.title)