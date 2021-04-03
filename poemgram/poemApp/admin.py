from django.contrib import admin
from poemApp.models import Poem, Comment, Like
from poemApp.models import UserProfile

admin.site.register(Poem)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserProfile)  # Is this needed?
