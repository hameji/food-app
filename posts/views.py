from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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