from django.db import models

# Create your models here.

class Todos(models.Model):
    task = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
