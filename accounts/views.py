from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLogoutView(BaseLogoutView):
    next_page = reverse_lazy('shop_home_page') 

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

# class CustomLogoutView(TemplateView):
#     template_name = 'registration/logout.html'

# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'

# def custom_logout(request):
#     auth_logout(request)
#     return redirect('login')  # Redirect to login page after logout

# def redirect_to_home(request):
#     return redirect('shop:home_page')
