from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    realname = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    instaID  = models.CharField(max_length=30)

    #profile_img = 
    #follower

    def __str__(self) -> str:
        return self.nickname