from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=UserManager)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.created(staff=instance)

@receiver(post_save,sender=UserManager)
def save_profile(sender,instance,**kwargs):
       instance.profile.save()       