from django.urls import path, include
from .views import index, SignUp
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='posts'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_form', views.PasswordResetForm, name='password_reset_form'),

]