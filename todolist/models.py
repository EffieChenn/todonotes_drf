from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
