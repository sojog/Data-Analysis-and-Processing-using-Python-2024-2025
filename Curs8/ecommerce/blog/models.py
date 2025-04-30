from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title


## MAKEMIGRATIONS
# CREATE TABLE BlogPost(id INT, title)


## MIGRATE
## executia