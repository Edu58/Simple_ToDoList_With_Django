from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import SignupView, LogoutView, PasswordResetView, PasswordChangeView, PasswordResetDoneView, PasswordResetFromKeyView, PasswordResetFromKeyDoneView

class SignupPage(SignupView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

class Logout(LogoutView):
    template_name = 'account/logout.html'

class ChangePassword(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account_login')

class ResetPassword(PasswordResetView):
    template_name = 'account/password_reset.html'

class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class ResetPasswordKey(PasswordResetFromKeyView):
    template_name = 'account/password_reset_from_key.html'

class ResetPasswordKeyDone(PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_from_key_done.html'