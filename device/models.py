from django.db import models

# Create your models here.
class Device(models.Model):
    device_id = models.CharField(max_length=50)
    device_creationTime = models.DateTimeField(auto_now_add=True)
    '''device_voltage = models.IntegerField(max_length=3)  # need to usedropdown 
    device_current = models.IntegerField(max_length=3)
    #device_chemistry = models.Char need to use dropdown, Lead Acid, LFP, NCA, NMC
    device_owner = models.CharField(max_length=100)
    device_phone = models.CharField(max_length=100)'''
