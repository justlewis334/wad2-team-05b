from django.db import models

class User(models.Model):
    userID=models.BigIntegerField(unique=True, null=False)
    name=models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=16, null=False)
    isAdmin = models.BooleanField(null=False)
    # forgot about this one...
    email = models.EmailField(null=False)
    
    def __str__(self):
        return self.name

class Poem(models.Model):
    poemID=models.BigIntegerField(unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.BigIntegerField(null=False, default=0)
    articleTitle = models.CharField(max_length=100, null=False)
    # on a second thought, storing the texts as a separate file is probably a good decision
    # I don't think either of the of the overloads are needed, but I'm not entirely sure
    text = models.FileField(null=False)

    def __str__(self):
        return self.articleTitle

class Comment(models.Model):
    commentID=models.BigIntegerField(unique=True, null=False)
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
