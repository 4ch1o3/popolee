from django.db import models
from account.models import Profile

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "publisher")
    image = models.ImageField(upload_to='images', blank=False)
    likecount = models.IntegerField(default = 0)
    headcount = models.IntegerField(default = 0)
    malecount = models.IntegerField(default = 0)
    femalecount = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "likes")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= "likes")
    
    class Meta:
        unique_together = ('post', 'profile')
