from django.contrib import admin

# Register your models here.

from .models import BlogPost

## Inregistrarea BlogPost-ului
admin.site.register(BlogPost)