from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyLoginView


urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]