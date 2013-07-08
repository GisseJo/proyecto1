from forum.models import *
from django.contrib import admin

class ForumAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "thread", "creator", "created"]

class ProfileAdmin(admin.ModelAdmin):
	list_display = ["user"]


admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, ProfileAdmin)