from django.shortcuts import render

# Create your views here.

def view_home(request):
    return render(request, 'home.html' )

def create_user(request):
    return render(request, 'user.html')