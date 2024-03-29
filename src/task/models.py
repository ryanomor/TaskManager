from django.db import models

# Create your models here.
class TaskItem(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    completed = models.BooleanField(blank=True, default=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
