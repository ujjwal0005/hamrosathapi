from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
   
     class Meta:
        model = Comment
        fields = ('id','user','blog','comment')
        extra_kwargs = {
            'comment': {'required': True},
        }

class BlogSerializer(serializers.ModelSerializer):
     image = serializers.ImageField(max_length=None, use_url=True)
     class Meta:
        model = Blog
        fields = ('id','user','title','content','image')
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
        }