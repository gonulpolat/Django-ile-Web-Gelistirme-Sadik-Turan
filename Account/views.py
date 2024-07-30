from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render

from Account.forms import LoginUserForm, NewUserForm

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
        form = NewUserForm(request.POST)

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
        form = NewUserForm()
        return render(request, 'account/register.html', {'form': form})

def UserLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out')
    return redirect("index")

def UserChangePassword(request):

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'You have successfully changed your password. Please login again')
            logout(request)
            return redirect("login")
        else:
            messages.add_message(request, messages.ERROR, 'Invalid password change')
            return render(request, 'account/change_password.html', {"form": form})

    form = PasswordChangeForm(user=request.user)

    return render(request, 'account/change_password.html', {"form": form})