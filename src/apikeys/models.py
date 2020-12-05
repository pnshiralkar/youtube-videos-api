from django.db import models

# Create your models here.


class ApiKey(models.Model):
    key = models.TextField()
    name = models.CharField(max_length=100, blank=True, null=True)