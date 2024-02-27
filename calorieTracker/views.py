from django.shortcuts import render

from .models import Food

def index(request):
    food = Food.objects.all()

    return render(request, 'calorieTracker/index.html', {'foods':food})
