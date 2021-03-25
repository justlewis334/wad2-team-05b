from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'poemApp/index.html')

def landingPage(request):
    return render(request,'poemApp/landingPage.html')

def login(request):
    return render(request,'poemApp/loginPage.html')
# Should the request page extend the inside or the outside base? Probably there's a better solution that either of these, but I'm not seeing it...
def about(request):
    return render(request,'poemApp/about.html')

