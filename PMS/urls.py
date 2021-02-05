from django.urls import path
from django.contrib.auth import views as auth_views
from PMS import views as PMS_views

from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('detail/', PMS_views.detail,name="detail"),
    #path('home/logout/', PMS_views.home,name="home"),
    path('Register/',views.Register,name="Register"),   
]


