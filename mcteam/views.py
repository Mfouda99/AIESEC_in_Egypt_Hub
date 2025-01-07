from django.shortcuts import render, redirect


def mcteam(request):
    return render(request, 'mcteam.html', {'form': 'form'})
