from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from .forms import (
    CustomUserLoginForm,
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomUserPasswordChangeForm,
)

from quizapp.models import User as QuizUser
from quizapp.utils import get_postfix



class AuthLogin(LoginView):
    
    form_class = CustomUserLoginForm
    template_name = "authapp/login.html"



class AuthRegister(CreateView):

    form_class = CustomUserCreationForm
    template_name = "authapp/register.html"
    success_url = reverse_lazy("authapp:login_page")



class AuthLogout(LogoutView, LoginRequiredMixin):
    
    ...



class AuthProfile(LoginRequiredMixin, UpdateView):

    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = "authapp/profile.html"
 

    def get_success_url(self):

        return reverse_lazy("authapp:profile_page", args=[self.request.user.pk])
    

    def get_object(self):
        return self.request.user
    


class AuthPasswordChange(PasswordChangeView):

    form_class = CustomUserPasswordChangeForm
    success_url = reverse_lazy("authapp:password_change_done_page")
    template_name = "authapp/password_change.html"



class AuthPasswordChangeDone(PasswordChangeDoneView):

    template_name = "authapp/password_change_done.html"