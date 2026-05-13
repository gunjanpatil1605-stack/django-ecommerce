from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post),
    path('comment/<int:post_id>/', views.add_comment),
    path('follow/<int:user_id>/', views.follow_user),
]