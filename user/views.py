from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .serializers import serializer
from .models import Customer
from rest_framework import generics

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def customerList(request):
    customers = Customer.objects.all()
    print(customers)
    return render(request, 'customers.html', {"customers":customers})


class customerFormAPI(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializer
