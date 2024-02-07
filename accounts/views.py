from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

login_view = LoginView.as_view(template_name='authentication/login.html')
logout_view = LogoutView.as_view(template_name='authentication/logout.html')

def redirect_to_home(request):
    return redirect('home_page')

def logout_view(request):
    auth_logout(request)
    return redirect('home_page')
