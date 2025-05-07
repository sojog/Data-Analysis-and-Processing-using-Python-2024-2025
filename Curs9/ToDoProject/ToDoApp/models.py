from django.db import models

# Create your models here.


class ToDoItem(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name