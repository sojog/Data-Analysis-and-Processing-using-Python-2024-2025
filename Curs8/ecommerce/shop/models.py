from django.db import models

# Create your models here.


### Product, title, description, slug

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title