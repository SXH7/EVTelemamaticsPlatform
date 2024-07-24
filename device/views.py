from django.shortcuts import render, redirect
from .forms import DeviceForm
from rest_framework import generics
from .models import Device
from .serializers import serializer

# Create your views here.
def registerDevice(request):

    print("Request method:", request.method)
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        print("POST data:", request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DeviceForm()
    return render(request, 'deviceRegister.html', {'form': form})

class resttest(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = serializer