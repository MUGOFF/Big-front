from django.db import models
from business.models import *
# Create your models here.
class User(models.Model):
    profile=models.ImageField(upload_to='account_profile_image', height_field=None, width_field=None, max_length=None, default='account_profile_image/deal2.png')
    back=models.ImageField(upload_to='account_profile_image', height_field=None, width_field=None, max_length=None, default='account_profile_image/napa.png')
    username= models.CharField(max_length=250, default="None")
    email= models.EmailField(max_length=250, default="anonymous@world.org")
    token= models.CharField(max_length=250, default="None", primary_key=True, unique=True)
    phone= models.CharField(max_length=11, default="None")
    intro = models.CharField(max_length=250, default="None")
    address= models.TextField(default="None")
    kind= models.TextField(default="None")
    job = models.TextField(default="None")
    kindPre= models.TextField(default="None")
    region= models.TextField(default="None")
    
    def __str__(self):
        return self.username
    
class Contract(models.Model):
    buyer_name = models.CharField(max_length=250, default="None")
    seller_name = models.CharField(max_length=250, default="None")
    buyer_birth = models.DateField(default='1900-01-01')
    seller_birth = models.DateField(default='1900-01-01')
    buyer_email = models.EmailField(max_length=250, default="anonymous@world.org")
    seller_email = models.EmailField(max_length=250, default="anonymous@world.org")
    buyer_address= models.TextField(default="None")
    seller_address= models.TextField(default="None")
    buyer_phone= models.CharField(max_length=11, default="None")
    seller_phone= models.CharField(max_length=11, default="None")
    farm_address= models.TextField(default="None")
    item= models.TextField(default="None")
    farm_area= models.IntegerField(default=0)
    farm_date= models.DateField(default='2023-01-01')
    payment_date= models.DateField(default='2023-01-01')
    payment= models.IntegerField(default=0)
    advance_date= models.DateField(default='2023-01-01')
    advance= models.IntegerField(default=0)
    interpay_date= models.DateField(default='2023-01-01')
    interpay= models.IntegerField(default=0)
    balance_date= models.DateField(default='2023-01-01')
    balance= models.IntegerField(default=0)
    goods_date= models.DateField(default='2023-01-01')
    special_contract = models.TextField(default="")
    document_date = models.DateField(auto_now_add=True)
    buyer_confirmed= models.BooleanField(default=False)
    seller_confirmed= models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.buyer_name + self.seller_name + self.item+str(self.document_date)    