from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    body = models.TextField()
