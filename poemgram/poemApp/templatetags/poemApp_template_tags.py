from django import template
from poemApp.models import UserProfile
from django.contrib.auth.models import User

register=template.Library()


@register.simple_tag
def getSlug(searchedUser):
    return UserProfile.objects.get(user=searchedUser).slug

