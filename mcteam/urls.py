from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('meet-mc-team/', views.mcteam, name='mcteam'),  
     
     ]