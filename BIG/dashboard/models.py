from django.db import models
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=250, default="익명")
    solvebool = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
class Answer(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)