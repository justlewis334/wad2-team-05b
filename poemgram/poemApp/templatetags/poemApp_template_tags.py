from django import template
from poemApp.models import Poem

register=template.Library()
## This might be important later on
##@register.inclusion_tag('poemApp/poems.html')
##def getPoems():
##    return {"poems": Poem.objects.all()}
