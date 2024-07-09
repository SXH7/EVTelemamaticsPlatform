from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):

    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')