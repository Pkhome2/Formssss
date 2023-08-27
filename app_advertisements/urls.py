
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name=''),
    path('top-sellers.html', top_sellers, name='top-sellers'),
    path('advertisement-post.html', advertisement_post, name='advertisement-post'),
    path('profile.html', profile, name='profile'),
    path('register.html', register, name='register'),
    path('login', login, name='login')


    ]