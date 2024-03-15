from django.urls import path
from .views import LogIn,signup,logOut,ProfileView,register
urlpatterns = [
    path('login/',LogIn,name='login'),
    path('signup/',register,name='signup'),
    path('logout/',logOut,name='logout'),
    path('profile/',ProfileView.as_view(),name='profile')
]
