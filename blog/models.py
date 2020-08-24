from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.title