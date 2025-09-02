from . import views
from django.urls import path
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('index/',views.index,name='index'),    
    path('register/', views.register, name='register'),
    path('log/', views.log, name='log'),
    path('intro/', views.intro, name='intro'),
    path('pottery/', views.pottery, name='pottery'),
    path('soft/', views.soft, name='soft'),
    path('wall_stickers/', views.wall_stickers, name='wall_stickers'),
    path('watch/', views.watch, name='watch'),
    path('jewelry/', views.jewelry, name='jewelry'),
    path('home_decor/', views.home_decor, name='home_decor'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('invoice/', views.invoice, name='invoice'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/<str:email>/<str:age>/<str:mobile>/', views.profile, name='profile'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('return_policy/', views.return_policy, name='return_policy'),
    path('privacy/', views.privacy, name='privacy'),
]