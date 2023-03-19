from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def say_hi(request):
    return render(request, 'users/hi.html')

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'There is an error with your credentials, please try again')
            return redirect('login')
    else:
        return render(request, 'users/auth/login.html')
    
def home(request):
    return render(request, 'users/home/user-dashboard.html')