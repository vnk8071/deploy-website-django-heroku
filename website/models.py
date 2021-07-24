from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title