from django import template
from poemApp.models import UserProfile, Comment
from django.contrib.auth.models import User

register=template.Library()


@register.simple_tag
def getSlug(searchedUser):
    return UserProfile.objects.get(user=searchedUser).slug


@register.simple_tag
def getReplies(comment):
    return getReplyAlg(comment, [])


def getReplyAlg(comment, clist):
    for i in  Comment.objects.filter(replyTo=comment):
        clist.append(i)
        getReplyAlg(i, clist)
    return clist
