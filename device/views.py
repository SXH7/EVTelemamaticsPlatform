from django.shortcuts import render, redirect
from .form import DeviceForm

# Create your views here.
def registerDevice(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            return redirect('/device/register')
    else:
        form = DeviceForm()
    return render(request, 'deviceRegister.html', {'form': form})
