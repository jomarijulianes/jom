from django.shortcuts import render

def index(request):
    return render(request,'pages/home.html')
def aboutpage(request):
    return render(request,'pages/about.html')
def servicespage(request):
    return render(request,'pages/services.html')
def contactpage(request):
    return render(request,'pages/contact.html')