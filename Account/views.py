from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def UserLogin(request):

    if request.user.is_authenticated:
        return redirect('index')

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

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'account/register.html', {'error': 'Username is already taken'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'account/register.html', {'error': 'Email is already taken'})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'account/register.html', {'error': 'Passwords do not match'})

    else:
        return render(request, 'account/register.html')

def UserLogout(request):
    logout(request)
    return redirect("index")
