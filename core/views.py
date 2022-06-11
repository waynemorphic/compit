from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_out(request):
    logout(request)
    return render(request, 'home/index.html')

# index template function
def index(request):
    return render(request, 'home/index.html')