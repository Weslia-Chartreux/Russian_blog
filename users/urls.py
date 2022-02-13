from django.urls import path, include
from users.views import SignUp, Password_Change, Password_Reset, Password_Reset_Complete, Password_Reset_Confirm, \
    Password_Reset_Done, Login_View, Logout_View
from django.contrib.auth import views

urlpatterns = [
    path('login/', Login_View.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('password_change/', Password_Change.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', Password_Reset.as_view(), name='password_reset'),
    path('password-reset/done/', Password_Reset_Done.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', Password_Reset_Confirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', Password_Reset_Complete.as_view(), name='password_reset_complete'),
    path('logout/', Logout_View.as_view(), name='logout'),

]
