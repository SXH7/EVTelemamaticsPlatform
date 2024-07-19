from django.db import models

# Create your models here.
class DataDump(models.Model):
    field1 = models.TextField(max_length=50, null=True)
    field2 = models.IntegerField(null=True)
    field3 = models.TextField(max_length=50, null=True)