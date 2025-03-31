from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Person(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.person.username
    
class Image(models.Model):
    publisher = models.OneToOneField(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=False)
    likes = models.IntegerField(default = 0)
    headcount = models.IntegerField(default = 0)
    malecount = models.IntegerField(default = 0)
    femalecount = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
