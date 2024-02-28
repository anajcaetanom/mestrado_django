from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    