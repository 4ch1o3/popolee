from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = models.EmailField('email address', unique=True)
    # email 필드 삭제 또는 사용하지 않음

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=30, unique=True)
    profile_image = models.ImageField(upload_to='profile', blank=False)

    def __str__(self) -> str:
        return self.nickname