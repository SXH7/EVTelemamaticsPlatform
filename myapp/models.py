from django.db import models

# Create your models here.
class DataDump(models.Model):
    x = models.TextField(max_length=50, null=True)