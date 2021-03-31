from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from poemApp.models import UserProfile


@receiver(post_save, sender=User)
def userHandler(sender, instance, created,  **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
