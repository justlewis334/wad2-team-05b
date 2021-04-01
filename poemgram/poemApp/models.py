from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django_extensions.db.fields import AutoSlugField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug=AutoSlugField(populate_from='user__username', slugify_function=slugify)

    def __str__(self):
        return self.slug

    
class Poem(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.BigIntegerField(null=False, default=0)
    articleTitle = models.CharField(max_length=100, null=True)
    text = models.TextField(null=False)
    addedDate = models.DateTimeField(auto_now_add=True, null=False)
    slug=AutoSlugField(populate_from='title', slugify_function=slugify)

    @classmethod
    def create(cls, title, user, text, articleTitle=None):
        return cls(title=title, user=user, text=text, articleTitle=articleTitle, likes=0)


    def __str__(self):
        return self.articleTitle

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    poem = models.ForeignKey(Poem, on_delete=models.SET_NULL, null=True)
    # just don't write a whole poem, it'll be fine
    text = models.TextField(null=False, default="")
    likes = models.BigIntegerField(null=False, default=0)
    # There isn't a good solution for on_delete
    # The "right" way to do it is that when a comment is deleted, only the text/username gets deleted
    # This way, the comment chain gets preserved
    replyTo = models.ForeignKey("self", on_delete=models.SET_DEFAULT, default=-1, related_name="comment")

    def __str__(self):
        return self.text
