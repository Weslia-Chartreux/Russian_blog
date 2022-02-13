from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordResetDoneView, LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = '/'
    template_name = 'signup.html'


class Password_Change(PasswordChangeView):
    template_name = 'password_change_form.html'


class Password_Reset(PasswordResetView):
    template_name = 'password_reset_form.html'


class Password_Reset_Complete(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class Password_Reset_Confirm(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'


class Password_Reset_Done(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class Login_View(LoginView):
    template_name = 'login.html'


class Logout_View(LogoutView):
    template_name = 'logged_out.html'
