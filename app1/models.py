from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    status = models.BooleanField(default=False)