from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


# Create your views here.
# view for home page
@never_cache
def home(request):
    if 'username' in request.session:
        name = request.session['username']
        return render(request, 'home.html', {'name': name, 'count': 1})
    else:
        return redirect(login)
# view for login page


@never_cache
def login(request):
    if 'username' in request.session:
        return redirect(home)
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            if username and password:
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    request.session['username'] = user.username
                    # auth_login(request, user)
                    return redirect(home)
                else:
                    # Authentication failed, set error message
                    error = "Invalid username or password. Please try again."
        except Exception as e:
            error = f"An unexpected error occurred during login. {e}"
    return render(request, 'login.html', {'error': error})
# view for log out page
# @require_POST


def logout_user(request):
    if request.method != 'POST':
        raise Http404("Page not found")
    if 'username' in request.session:
        request.session.flush()
        return redirect(login)
