from django import template
from poemApp.models import UserProfile
from django.contrib.auth.models import User

register=template.Library()
## This might be important later on
##@register.inclusion_tag('poemApp/poems.html')
##def getPoems():
##    return {"poems": Poem.objects.all()}


@register.simple_tag
def getSlug(searchedUser):
    return UserProfile.objects.get(user=searchedUser).slug
