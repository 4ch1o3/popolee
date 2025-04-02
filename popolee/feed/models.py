from django.db import models
from account.models import Profile

class Image(models.Model):
    publisher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "images")
    image = models.ImageField(upload_to='images', blank=False)
    likes = models.IntegerField(default = 0)
    headcount = models.IntegerField(default = 0)
    malecount = models.IntegerField(default = 0)
    femalecount = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
