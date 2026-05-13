from django.contrib import admin
from .models import Profile, Post, Like, Comment, Follow


# 👤 Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']


# 📝 Post Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']


# ❤️ Like Admin
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


# 💬 Comment Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'created_at']
    search_fields = ['text']


# 👥 Follow Admin
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following']
