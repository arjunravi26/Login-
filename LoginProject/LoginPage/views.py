from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


# View for the home page
@never_cache
# Ensures only logged-in users can access the home page
@login_required  
def home(request):
    name = request.user.username
    return render(request, 'home.html', {'name': name})

# View for the login page
@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('home') 

    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                error = "Invalid username or password. Please try again."
        else:
            error = "Please enter both username and password."
    return render(request, 'login.html', {'error': error})

# View for logging out
# Ensures logout can only be triggered by a POST request
@require_POST 
def logout_user(request):
    auth_logout(request)
    return redirect('login')