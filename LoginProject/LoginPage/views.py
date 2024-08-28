from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


# Create your views here.
@never_cache
def home(request):
    if 'username' in request.session:
        name = request.session['username']
        return render(request, 'home.html', {'name': name})
    else:
        return redirect(login)
@never_cache
def login(request):
    if 'username' in request.session:
        return redirect(home)
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username'] = user.username
                # auth_login(request, user)
                return redirect(home)
            else:
                # Authentication failed, set error message
                error = "Invalid username or password. Please try again."
        except Exception as e:
            error = "An unexpected error occurred during login."
    return render(request, 'login.html', {'error': error})
# @require_POST
def logout_user(request):
    if request.method != 'POST':
        raise Http404("Page not found")
    if 'username' in request.session:
        request.session.flush()
        return redirect(login)

# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect, render
# from HomePage.views import home


# # Create your views here.
# def login(request):
#     # form = LoginForm()
#     if request.POST:
#         # frm = LoginForm(request.POST)
#         # if frm.is_valid():
#         #     print("success")
#         #     frm.save()
#         # else:
#         #     print("some error")
#         data = request.POST
#         user_name = data.get('username')
#         password = data.get('password')
#         print(authenticate(user_name,password))
#     e)
    #     return rendr(request, 'login.html'
    #         redirect(home)
    #     return render(request, 'login.html')
    #     return render(request, 'login.html')
