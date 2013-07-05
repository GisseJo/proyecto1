
from blog.models import *
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]
    

admin.site.register(Comment, CommentAdmin)

admin.site.register(Post, PostAdmin)