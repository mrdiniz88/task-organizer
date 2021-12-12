from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
]
