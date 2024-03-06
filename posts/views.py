from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import PostCreateForm
from .models import Post
from users.models import Profile

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/create.html', {'form': form})

@login_required
def index(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    posts = Post.objects.filter(user=current_user)
    return render(request, 'posts/index.html', {'posts': posts, 'profile': profile})

def feed(request):
    posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts': posts})

def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user.id)
    else:
        post.liked_by.add(request.user.id)
    return