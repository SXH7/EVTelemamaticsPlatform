from django.shortcuts import render, redirect
from myapp.models import DataDump 


# Create your views here.
def home(request):

    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')

def raw(request):
    data = DataDump.objects.all()
    if request.user.is_authenticated:
        return render(request, 'raw.html', {'data': data})
    else:
        return redirect('login')

def assets(request):

    if request.user.is_authenticated:
        return render(request, 'assets.html')
    else:
        return redirect('login')