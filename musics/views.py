from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Music

# Create your views here.
def music_list(request):
    music_objects = Music.objects.all()
    paginator = Paginator(music_objects, 5)
    page = request.GET.get('page')
    music_objects = paginator.get_page(page)
    return render(request, 'musics/music_list.html', {'music_objects': music_objects})