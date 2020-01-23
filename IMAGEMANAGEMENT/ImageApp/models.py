from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000)
    image = models.FileField(upload_to='post_image', blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)


        def __str__(self):
            return self.name
