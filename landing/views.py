from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages




def landing(request):
   return render(request, 'landing.html', {'name': 'landing'})
