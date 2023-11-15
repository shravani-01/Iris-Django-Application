from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'index.html')

def user(request):
    username=request.GET['username']
    print(username)
    return render(request, 'user.html', {'name':username})