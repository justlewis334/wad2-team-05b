from django.contrib import admin
from poemApp.models import Poem, Comment, UserProfile

admin.site.register(Poem)
admin.site.register(Comment)
admin.site.register(UserProfile)  # Is this needed?
