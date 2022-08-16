from account.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog')
    image = models.ImageField(upload_to='media',null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_comment')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField()
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}-{self.blog}'

