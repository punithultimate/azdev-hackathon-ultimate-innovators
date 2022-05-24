from . import views
from django.urls import path

urlpatterns = [
    path('',views.intro,name="intro"),
    path('profiles/',views.profiles,name="profiles"),
    path('profile/<str:pk>/',views.userprofile,name="user-profile"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
]
