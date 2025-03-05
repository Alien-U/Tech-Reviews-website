from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.timezone import now
# from .models import Post
# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    # desc = models.CharField(max_length=3000)
    desc=HTMLField()
    pub_date = models.DateField()
    image=models.ImageField(upload_to="shome/images",default="")

    def __str__(self):
        return self.product_name
class Softwarez(models.Model):
    software_id = models.AutoField
    software_name = models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="shome/images",default="")

    def __str__(self):
        return self.software_name
class Gaming(models.Model):
    game_id = models.AutoField
    game_name = models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="shome/images",default="")

    def __str__(self):
        return self.game_name
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    subject=models.CharField(max_length=50,default="")
    message=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.name

# class BlogComment(models.Model):
#     sno=models.AutoField(primary_key=True)
#     comment=models.TextField()
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     post=models.ForeignKey(Gaming,on_delete=models.CASCADE)
#     parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
#     timestamp=models.DateTimeField(default=now)