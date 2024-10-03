from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=150)
    content = models.TextField()
    like = models.ManyToManyField(User, blank=True, related_name='blog_like')
    
    def __str__(self):
        return self.title
    
class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"comment by {self.user.username} on {self.blog.title}"
    
class faq(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1050)
    
    def __str__(self):
        return self.question
    
class reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(faq, on_delete=models.CASCADE)
    reply = models.TextField()
    
    def __str__(self):
        return f"reply by {self.user} on {self.question}"