from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def UserLogin(request):

    if request.user.is_authenticated and "next" in request.GET:
        messages.add_message(request, messages.ERROR, 'You must be logged out to login as admin')
        return render(request, 'account/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You have successfully logged in')
            nextUrl = request.GET.get('next', None)
            if nextUrl is None:
                return redirect('index')
            else:
                return redirect(nextUrl)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return render(request, 'account/login.html')
    else:
        return render(request, 'account/login.html')

def UserRegister(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            return render(request, 'account/register.html', 
                          {'error': 'Passwords do not match',
                           "username": username,
                           "email": email
                           })
        if User.objects.filter(username=username).exists():
            return render(request, 'account/register.html', 
                          {'error': 'Username is already taken',
                           "email": email
                           })
        if User.objects.filter(email=email).exists():
            return render(request, 'account/register.html', 
                          {'error': 'Email is already taken',
                           "username": username
                           })
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')        

    else:
        return render(request, 'account/register.html')

def UserLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out')
    return redirect("index")
