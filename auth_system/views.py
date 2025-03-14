from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "auth_system/register.html"
    success_url = reverse_lazy("index")


class UserLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'auth_system/login.html'
    success_url = reverse_lazy('task-list')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(f"Kористувач {request.user.username} виходить")
        else:
            print("Користувач не аутентифікований, але намагався вийти")
        # print("Користувач вийшов:", request.user.username)  # Вивід логування
        return super().dispatch(request, *args, **kwargs)
    
class ProfileView(TemplateView):
    template_name = 'portfolio/portfolio.html'