from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog_images")
    body  = models.TextField()

    def __str__(self):
        return self.title 