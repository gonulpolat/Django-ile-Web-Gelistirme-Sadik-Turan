from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.add_message(request, messages.SUCCESS, 'You have successfully registered')

            return redirect('index')
        
        else:
            return render(request, 'account/register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

def UserLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out')
    return redirect("index")
