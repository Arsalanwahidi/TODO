from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

