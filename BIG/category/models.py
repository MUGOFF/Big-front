from django.db import models

# Create your models here.
class Carrot(models.Model):
    date = models.DateField(primary_key=True,unique=True)
    value = models.FloatField(default=0.0)
    estimated_value_low = models.FloatField(default=0.0)
    estimated_value_high = models.FloatField(default=0.0)
    
    def __unicode__(self):
        return self.date
    
class Seoul(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
    
class Gwanju(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class Daegu(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class Daejun(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class Pusan(models.Model):
    ds = models.DateField()
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()

    def __str__(self):
        return str(self.ds)+self.item


class SeoulAPI(models.Model):
    ds = models.DateField()
    price = models.FloatField(default=0.0)
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class PusanAPI(models.Model):
    ds = models.DateField()
    price = models.FloatField(default=0.0)
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class DaeguAPI(models.Model):
    ds = models.DateField()
    price = models.FloatField(default=0.0)
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class DaejunAPI(models.Model):
    ds = models.DateField()
    price = models.FloatField(default=0.0)
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item
class GwanjuAPI(models.Model):
    ds = models.DateField()
    price = models.FloatField(default=0.0)
    ythat = models.FloatField(default=0.0)
    yhat_lower = models.FloatField(default=0.0)
    yhat_upper = models.FloatField(default=0.0)
    item = models.TextField()
    
    def __str__(self):
        return str(self.ds)+self.item