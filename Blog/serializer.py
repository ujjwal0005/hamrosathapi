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
    class Meta:
        model = Blog
        fields = ('id','user','title','content','image')

