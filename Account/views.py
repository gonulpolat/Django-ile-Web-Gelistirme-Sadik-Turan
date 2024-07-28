from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.

def UserLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'account/login.html')

def UserRegister(request):
    return render(request, 'account/register.html')

def UserLogout(request):
    return redirect("index")
