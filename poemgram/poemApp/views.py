from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

def index(request):
    return render(request,'poemApp/index.html')

def landingPage(request):
    return render(request,'poemApp/landingPage.html')

def login(request):
    return render(request,'poemApp/loginPage.html')

def about(request):
    return render(request,'poemApp/about.html')

# based on https://www.pluralsight.com/guides/work-with-ajax-django

def checkUserName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        userName = request.GET.get("username", None)
        # check for the nick name in the database.
        print(User.objects.filter(username = userName).exists())
        print(userName)
        if User.objects.filter(username = userName).exists():
            return JsonResponse("Please choose another username", status = 200, safe=False)
        else:
            return JsonResponse("true", status = 200, safe=False)

    return JsonResponse({}, status = 400)
