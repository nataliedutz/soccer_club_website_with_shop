from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from .models import Profile
from .forms import ProfileForm
from shop.models import Order 
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            messages.success(request, 'Your account has been created successfully. Please log in.')  # Notify user about successful registration
            return redirect('login')  # Redirect to login page after registration
        else:
            # If form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')  # Notify user about form errors
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLogoutView(BaseLogoutView):
    next_page = reverse_lazy('team:home_page') 

    def dispatch(self, request, *args, **kwargs):
        # Handle logout explicitly
        auth_logout(request)
        return redirect(self.next_page)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify your login template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(profile=profile)
    return render(request, 'registration/profile.html', {'profile': profile, 'orders': orders})


def edit_profile(request):
    profile = request.user.profile  # Assuming profile is related to the logged-in user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful editing
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})

# class CustomLogoutView(TemplateView):
#     template_name = 'registration/logout.html'

# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'

# def custom_logout(request):
#     auth_logout(request)
#     return redirect('login')  # Redirect to login page after logout

# def redirect_to_home(request):
#     return redirect('shop:home_page')
