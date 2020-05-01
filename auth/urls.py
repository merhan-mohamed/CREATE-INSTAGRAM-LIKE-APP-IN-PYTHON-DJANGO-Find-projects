from django.urls import path

from Insta.auth import views

urlpatterns = [
    path('Login/', views.LoginView.as_view(), name='Login'),
    path('Logout/', views.LogoutView.as_view(), name='Logout'),
    path('Register/',views.RegisterView.as_view(), name='Register'),
    path('me/', views.UserView.as_view(), name='user')
    ]