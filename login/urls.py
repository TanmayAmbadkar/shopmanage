from login.views import LoginView, SignUpView, LogoutView
from django.urls import path

urlpatterns = [
        path('login', LoginView.as_view(), name='login'),
        path('signup', SignUpView.as_view(), name='signup'),
        path('logout', LogoutView.as_view(), name='logout'),
    ]
