from django.urls import path
from .views import SignupPage, Logout, ResetPassword, ChangePassword, ResetPasswordDone

urlpatterns = [
    path('signup/', SignupPage.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('change/', ChangePassword.as_view(), name='pass_change'),
    path('reset/', ResetPassword.as_view(), name='pass_reset'),
    path('reset/login', ResetPasswordDone.as_view(), name='pass_reset_done'),
]
