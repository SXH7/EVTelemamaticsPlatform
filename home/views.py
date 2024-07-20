from django.shortcuts import render, redirect
from myapp.models import DataDump 
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


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

def chargers(request):

    if request.user.is_authenticated:
        return render(request, 'chargers.html')
    else:
        return redirect('login')

@require_http_methods(["GET"])
def grafana_proxy(request):
    username = 'admin'
    password = 'admin'
    grafana_url = 'http://localhost:3000/goto/R_p7tdXIR?orgId=1'

    response = requests.get(grafana_url, auth=HTTPBasicAuth(username, password))
    return HttpResponse(response.content, content_type='text/html')