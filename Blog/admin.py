from django.contrib import admin
from .models import Blog,Comment



# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # form_class = CustomUserCreationForm
    list_display=['id','user','title']
    list_display_links=['id','title',]
    ordering = ['-id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # form_class = CustomUserCreationForm
    list_display=['id','user','comment']
    list_display_links=['user','comment',]
    ordering = ['id']
