from django.shortcuts import render

from .models import Forum

# Create your views here.
def bic_forum(request):
    clothing_list = Forum.objects.filter(category=0)
    food_list = Forum.objects.filter(category=1)
    housing_list = Forum.objects.filter(category=2)
    else_list = Forum.objects.filter(category=3)
    context = {
        'clothing_list': clothing_list,
        'food_list': food_list,
        'housing_list': housing_list,
        'else_list': else_list,
    }
    return render(request, 'bic/forum_list.html', context)
