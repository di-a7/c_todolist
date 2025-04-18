from django.db import models

# Create your models here.
class Todolist(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   is_completed = models.BooleanField(default=False)