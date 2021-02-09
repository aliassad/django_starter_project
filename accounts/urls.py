from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.RegisterUser.as_view(template_name='accounts/register.html'), name='register'),
]
