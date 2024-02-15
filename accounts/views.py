from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout as auth_logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

login_view = LoginView.as_view(template_name='registration/login.html')
logout_view = LogoutView.as_view()

def custom_logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout

def redirect_to_home(request):
    return redirect('home_page')
