from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.contrib.auth.models import User
from poemApp.models import Poem, UserProfile, Comment
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# this was preinstalled for me, if you need it, you can download it with "pip install requests"
import requests
import random
import re


#this is the view of the index page, the intial page when opening the app
@login_required
def index(request):
    contextDict={}
    try:
        contextDict["randPoem"]=randPoem = random.choice(Poem.objects.all())
        contextDict["rrows"]=randPoem.text.split("\n")
    except:
        randPoem=None
    contextDict["recent"]=Poem.objects.order_by("-addedDate")[:8]
    contextDict["mostLikes"]=Poem.objects.order_by("-likes")[:8]
    return render(request,'poemApp/index.html', context=contextDict)

#this is the view of the landing page 
def landingPage(request):
    mostLiked = Poem.objects.order_by("-likes").first()
    contextDict={}
    if mostLiked!=None:
        contextDict["title"]=mostLiked.title
        contextDict["rows"]=mostLiked.text.split("\n")
        contextDict["author"]=mostLiked.user.username
        contextDict["obj"] = mostLiked
    return render(request,'poemApp/landingPage.html', context=contextDict)
#view for login page 
def login(request):
    return render(request,'poemApp/loginPage.html')

def about(request):
    return render(request,'poemApp/about.html')

@login_required
def showUserprofile(request, usernameSlug):
    contextDict={}
    try:
        contextDict["user"]= UserProfile.objects.get(slug=usernameSlug).user
        contextDict["poems"] = Poem.objects.filter(user=contextDict["user"])
        contextDict["about"]= UserProfile.objects.get(slug=usernameSlug).about
    except:
        contextDict["user"]= None
        contextDict["poems"]= None
    return render(request,'poemApp/userprofile.html', context=contextDict)

@login_required
def preCompose(request):
    # Doing this in JS would have exposed my API key
    mykey="c871909d1ffead4f16cafa1d2fc5e42a23d6eb6d"
    # none is false
    if request.GET.get("url") or request.GET.get("text"):
        if request.GET.get("url")=="":
            return compose(request)
        else:
            response=requests.get("https://extractorapi.com/api/v1/extractor/?apikey="+mykey+"&url="+request.GET.get("url")).json()
            if response["status_code"]==200:
                base_url = reverse('poemApp:compose')
                query_string =  urlencode({'text': response["text"]}) + "&" + urlencode({'title': response["title"]})
                return  redirect(base_url+"?"+query_string)
            else:
                return render(request,'poemApp/precompose.html', context={"badUrl":"True"})

    else:
        return render(request,'poemApp/precompose.html')
            
        
        
    contextDict={}
    
@login_required
def compose(request):
    if request.GET.get("text")==None:
        return preCompose(request)
    else:
        contextDict={}
        contextDict["title"]=request.GET.get("title")
        contextDict["text"]=re.findall(r'\w+', request.GET.get("text"))
        random.shuffle(contextDict["text"])
        return render(request,'poemApp/compose.html', context=contextDict)
    
@login_required
def search(request):
    contextDict={}

    if request.GET.get('type')=="Poem":
        contextDict["type"]="Poem"
        contextDict["list"]= Poem.objects.filter(text__icontains=request.GET.get('search'))
    else:
        contextDict["type"]="User"
        contextDict["list"]= User.objects.filter(username__icontains=request.GET.get('search'))

    return render(request,'poemApp/searchResult.html', context=contextDict)
#the view for the poem page 
@login_required
def poem(request, poemSlug):
    contextDict={}
    try:
        contextDict["poem"]= Poem.objects.get(slug=poemSlug)
        contextDict["rows"]= Poem.objects.get(slug=poemSlug).text.split("\n")
        contextDict["comments"] = Comment.objects.filter(poem=contextDict["poem"])
    except:
        contextDict["poem"]= None
        contextDict["rows"]= None
    return render(request, "poemApp/poemPage.html", context=contextDict)

@login_required
def submitPoem(request):
    p=Poem.create(request.POST.get("title"), request.user, request.POST.get("poem"), request.POST.get("articleTitle"))
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


@login_required
def like_unlike(request):
    # Request must be POST
    if request.method == "POST":
        obj_id = request.POST.get('obj_id')
        # request.user is the actual record, not just an username
        user_prof = request.user
        if request.POST.get('type')=="poem":
            obj = Poem.objects.get(id=obj_id)
        else:
            obj = Comment.objects.get(id=obj_id)

        if user_prof in obj.likes.all():
            obj.likes.remove(user_prof)
            newStatus="Like"
        else:
            obj.likes.add(user_prof)
            newStatus="Dislike"

        data = {
            'likes': obj.likes.all().count(),
            'newStatus': newStatus
        }
        
        return JsonResponse(data, safe=False)
    return JsonResponse({'success': 'false'})

@login_required
def submitComment(request):
    if request.method == "POST":
        print(request.POST.get("poem"))
        print(request.POST.get("text"))
        newComment = Comment.create(Poem.objects.get(id=int(request.POST.get("poem"))), request.user,  request.POST.get("text"))
        newComment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
