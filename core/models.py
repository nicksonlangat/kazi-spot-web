from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    description=models.TextField()
    detail=models.CharField(max_length=100)

    def __str__(self):
        return self.title
