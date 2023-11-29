
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_register, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]