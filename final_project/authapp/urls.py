from django.urls import path

from . import views


app_name = "orders"

urlpatterns = [
    path("login/", views.AuthLogin.as_view(), name="login_page"),
    path("register/", views.AuthRegister.as_view(), name="register_page"),
    path("logout/", views.AuthLogout.as_view(), name="logout_page"),
    path("profile/", views.AuthProfile.as_view(), name="profile_page"),
    path('password-change/', views.AuthPasswordChange.as_view(), name='password_change_page'),
    path('password-change/done/', views.AuthPasswordChangeDone.as_view(), name='password_change_done_page'),
]