from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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
    # getting current user
    if request.user.is_authenticated:
        current_user = request.user
    else:
        print('Unauthenticated user')
    
    user_data = User.objects.get(username=current_user.username)

    welcome_text = 'Greetings ' + user_data.first_name + ' ' + user_data.last_name
    last_login = user_data.last_login
    return render(request, 'users/home/user-dashboard.html', {
        'welcome_text': welcome_text,
        'last_login_time': last_login,
    })