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
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Blog
        fields = ('id','user','title','content','image','image_url')
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
        }

    def get_image_url(self, obj):
        return obj.image.url
