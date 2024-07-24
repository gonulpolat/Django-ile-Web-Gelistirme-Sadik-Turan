from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl = models.CharField(max_length=100)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
