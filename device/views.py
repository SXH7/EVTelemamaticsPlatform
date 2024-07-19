from django.shortcuts import render, redirect
from .forms import DeviceForm

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
