# accounts/urls.py
from django.urls import path

from .views import SignUpView, change_password

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('change-password/', change_password, name='change_password'),
]