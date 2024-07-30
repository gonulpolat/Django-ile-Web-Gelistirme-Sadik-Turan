from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from Account.forms import LoginUserForm

# Create your views here.

def UserLogin(request):

    if request.user.is_authenticated and "next" in request.GET:
        messages.add_message(request, messages.ERROR, 'You must be logged out to login as admin')
        return render(request, 'account/login.html')

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
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
                return render(request, 'account/login.html', {'form': form})
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form})

def UserRegister(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            return render(request, 'account/register.html', 
                          {"username": username,
                           "email": email
                           })
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Username is already taken')
            return render(request, 'account/register.html',{"email": email})
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email is already taken')
            return render(request, 'account/register.html', {"username": username})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User created successfully')
        return redirect('login')        

    else:
        return render(request, 'account/register.html')

def UserLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out')
    return redirect("index")
