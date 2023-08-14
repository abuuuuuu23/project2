from django.shortcuts import render
def base(request):
    return render(request,'base.html')
def apps(request):
    return render(request,'apps.html')
def login(request):
    return render(request,'login.html')
# Create your views here.
