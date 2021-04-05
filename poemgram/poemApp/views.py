from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.contrib.auth.models import User
from poemApp.models import Poem, UserProfile, Like
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
# this was preinstalled for me, if you need it, you can download it with "pip install requests"
import requests
import random
import re



@login_required
def index(request):
    contextDict={}
    randPoem = random.choice(Poem.objects.all())
    if randPoem!=None:
        contextDict["rtitle"]=randPoem.title
        contextDict["rrows"]=randPoem.text.split("\n")
        contextDict["rauthor"]=randPoem.user.username
        contextDict["obj"] = randPoem
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
        contextDict["obj"] = mostLiked
    return render(request,'poemApp/landingPage.html', context=contextDict)

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
        contextDict["obj"] = Poem.objects
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
        contextDict["text"]=[]
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

@login_required
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


@login_required
def poem_like_unlike(request):
    user = request.user
    # Request must be POST
    if request.method == "POST":
        poem_id = request.POST.get('poem_id')
        poem = Poem.objects.get(id=poem_id)
        user_prof = User.objects.get(username=user)

        if user_prof in poem.likes.all():
            poem.likes.remove(user_prof)
        else:
            poem.likes.add(user_prof)

        like, created = Like.objects.get_or_create(user=user_prof, poem_id=poem_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Dislike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            poem.save()
            like.save()

        data = {
            'value': like.value,
            'likes': poem.likes.all().count()
        }
        return JsonResponse(data, safe=False)
    return JsonResponse({'success': 'false'})
