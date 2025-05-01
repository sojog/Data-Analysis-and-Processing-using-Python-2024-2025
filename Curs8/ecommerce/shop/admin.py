from django.contrib import admin

# Register your models here.

from .models import Product

## Inregistrarea BlogPost-ului
admin.site.register(Product)