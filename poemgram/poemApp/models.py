from django.db import models
from django.contrib.auth.models import User

# Sike, turns out I was trying to reinvent the wheel with the user model


class Poem(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.BigIntegerField(null=False, default=0)
    articleTitle = models.CharField(max_length=100, null=True)
    text = models.TextField(null=False)
    addedDate = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.articleTitle

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    poem = models.ForeignKey(Poem, on_delete=models.SET_NULL, null=True)
    # just don't write a whole poem, it'll be fine
    text = models.CharField(max_length=1000, null=False, default="")
    likes = models.BigIntegerField(null=False, default=0)
    # There isn't a good solution for on_delete
    # The "right" way to do it is that when a comment is deleted, only the text/username gets deleted
    # This way, the comment chain gets preserved
    replyTo = models.ForeignKey("self", on_delete=models.SET_DEFAULT, default=-1, related_name="comment")

    def __str__(self):
        return self.text
