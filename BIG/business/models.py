from django.db import models
import django
# Create your models here.
class Futures_article(models.Model):
    profile =models.ImageField(upload_to='Future_Article_profile_image', height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=250, default="title")
    seller_name = models.CharField(max_length=250, default='홍길동')
    seller_email = models.EmailField(max_length=250, default='anonymous@world.org')
    g_date = models.DateField(default=django.utils.timezone.now)
    item = models.CharField(max_length=250, default='None')
    region = models.CharField(max_length=250, default='None')
    sub_region = models.CharField(max_length=250, default='None')
    quality = models.CharField(max_length=250, default='None')
    area = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, default='')
    # base64 = models.TextField(blank=True, default='')
    # img_name = models.CharField(max_length=250, default='None')
    
    def __str__(self):
        return self.seller_name +self.item