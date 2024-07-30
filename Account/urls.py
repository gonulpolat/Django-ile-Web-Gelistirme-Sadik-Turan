from django.urls import path

from Account import views


urlpatterns = [
    path('login', views.UserLogin, name='login'),
    path('register', views.UserRegister, name='register'),
    path('logout', views.UserLogout, name='logout'),
    path('change-password', views.UserChangePassword, name='change_password'),
]