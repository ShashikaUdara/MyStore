from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.say_hi, name='hi'),
    path('user_login/', views.user_login, name='login'),
]
