from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from poemApp.models import Poem, UserProfile
from django.template.defaultfilters import slugify
from django.views.generic.list import ListView
from django.shortcuts import redirect
import random

def index(request):
    contextDict={}
    randPoem = random.choice(Poem.objects.all())
    if randPoem!=None:
        contextDict["rtitle"]=randPoem.title
        contextDict["rrows"]=randPoem.text.split("\n")
        contextDict["rauthor"]=randPoem.user.username
    contextDict["recent"]=Poem.objects.order_by("-addedDate")[:8]
    contextDict["mostLikes"]=Poem.objects.order_by("-likes")[:8]
    return render(request,'poemApp/index.html', context=contextDict)

def landingPage(request):
    mostLiked = Poem.objects.order_by("-likes").first()
    contextDict={}
    if mostLiked!=None:
        contextDict["title"]=mostLiked.title
        contextDict["rows"]=mostLiked.text.split("\n")
        contextDict["author"]=mostLiked.user.username
    return render(request,'poemApp/landingPage.html', context=contextDict)

def login(request):
    return render(request,'poemApp/loginPage.html')

def about(request):
    return render(request,'poemApp/about.html')

def showUserprofile(request, usernameSlug):
    contextDict={}
    try:
        contextDict["user"]= UserProfile.objects.get(slug=usernameSlug).user
        contextDict["poems"] = Poem.objects.filter(user=contextDict["user"])
    except:
        contextDict["user"]= None
        contextDict["poems"]= None
    return render(request,'poemApp/userprofile.html', context=contextDict)

def compose(request):
    contextDict={}
    return render(request,'poemApp/compose.html', context=contextDict)

def search(request):
    contextDict={}

    if request.GET.get('type')=="Poem":
        contextDict["type"]="Poem"
        contextDict["list"]= Poem.objects.filter(text__icontains=request.GET.get('search'))
    else:
        contextDict["type"]="User"
        contextDict["list"]= User.objects.filter(username__icontains=request.GET.get('search'))

    return render(request,'poemApp/searchResult.html', context=contextDict)

def submitPoem(request):
    p=Poem.create(request.POST.get("title"), request.user, request.POST.get("poem"), "asdsada")
    p.save()
    return redirect("/poemApp/index")
    
# based on https://www.pluralsight.com/guides/work-with-ajax-django

def checkUserName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        userName = request.GET.get("username", None)
        # check for the nick name in the database.
        if User.objects.filter(username = userName).exists():
            return JsonResponse("Please choose another username", status = 200, safe=False)
        else:
            return JsonResponse("true", status = 200, safe=False)

    return JsonResponse({}, status = 400)
