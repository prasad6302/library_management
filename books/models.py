from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.title