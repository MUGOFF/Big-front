from django.db import models
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    written_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ('-written_date',)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/{self.title}/'
    

class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    written_date = models.DateField(auto_now_add=True)
    recent_updated = models.DateField(auto_now=True)
    writer = models.CharField(max_length=250, default="익명")
    writer_email = models.EmailField(max_length=250, default="anaonymous@gmail.org")
    solvebool = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20, default="ADMIN")
    message = models.TextField()
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return "질문 id: "+ str(self.post.id) +self.post.title+"-> 답변"