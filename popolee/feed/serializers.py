from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    publisher = serializers.CharField(source='profile.nickname')  

    class Meta:
        model = Post
        fields = [
            'id', 'publisher', 'image',
            'likecount', 'headcount', 'malecount', 'femalecount', 'created_at'
        ]
