from django.contrib import admin
from .models import UserProfile, SubHub, Post, Comment


admin.site.register(UserProfile)
admin.site.register(SubHub)
admin.site.register(Post)
admin.site.register(Comment)