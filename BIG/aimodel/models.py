from django.db import models

# Create your models here.
class Aimodel(models.Model):
    file = models.FileField()
    version = models.CharField(max_length=100)
    select = models.BooleanField(default=False)
    item = models.TextField(default='')
    region = models.TextField(default='')
    cap = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
class Result(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item