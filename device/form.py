from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = {'device_id'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)