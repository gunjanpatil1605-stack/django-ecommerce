from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Like, Comment, Follow


# 🏠 Home Page (Feed)
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


# 📝 Create Post (with image support)
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Post.objects.create(
            user=request.user,
            content=content,
            image=image
        )
    return redirect('home')


# ❤️ Like / Unlike Post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()   # unlike
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('home')


# 💬 Add Comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect('home')


# 👥 Follow / Unfollow User
@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)

    follow = Follow.objects.filter(
        follower=request.user,
        following=user_to_follow
    )

    if follow.exists():
        follow.delete()   # unfollow
    else:
        Follow.objects.create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect('home')