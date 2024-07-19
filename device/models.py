from django.db import models

# Create your models here.
class Device(models.Model):

    VOLTAGE = [
        (400, "400V"),
        (500, "500V"),
        (600, "600V"),
    ]

    CHEMISTRY = [
        ('Lithium Ion', 'Lithium Ion'),
        ('Lead Acid', 'Lead Acid'),
        ('NCA', 'NCA'),
        ('NMC', 'NMC'),
    ]

    device_id = models.CharField(max_length=50)
    device_creationTime = models.DateTimeField(auto_now_add=True)
    device_voltage = models.IntegerField(choices=VOLTAGE, null=True)  
    device_current = models.IntegerField()
    device_chemistry = models.CharField(choices=CHEMISTRY, null=True)
    device_owner = models.CharField(max_length=100)
    device_phone = models.CharField(max_length=100)
