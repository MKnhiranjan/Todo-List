from django.db import models

# Create your models here.
class Todo(models.Model):
    topic=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.topic
    