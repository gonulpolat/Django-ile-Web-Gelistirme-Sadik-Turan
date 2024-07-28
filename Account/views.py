from django.shortcuts import redirect, render

# Create your views here.

def UserLogin(request):
    return render(request, 'account/login.html')

def UserRegister(request):
    return render(request, 'account/register.html')

def UserLogout(request):
    return redirect("index")
