
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import GraphDescrip.views
from . import views
urlpatterns = [
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('', GraphDescrip.views.home, name = 'home'),
    path('loggedin', views.loggedin, name = 'loggedin'),
]
