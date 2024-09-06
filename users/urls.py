from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path,include
from . import views


class PasswordResetViewDone:
    pass


urlpatterns = [
    path('login/',views.LoginUser.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('profile/', views.ProfileUser.as_view(),name='profile'),
    path('password_change/',views.ChangePassword.as_view(),name='password_change'),
    path('password_change/done',PasswordChangeDoneView.as_view(template_name='user/password_change_form_done.html'), name='password_change_done'),
    path('password_reset_application/',PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset_form'),
    path('password_reset_application/done',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-confirm/complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete')


]