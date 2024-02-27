from django.shortcuts import render

from .models import Food, Consume

def index(request):
    food = Food.objects.all()
    consumed_foods = []
    if request.method == "POST":
        food_consumed = request.POST['food_consumed'] # gives back just the name
        consumed_object = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consumed_object)
        consume.save()
        consumed_foods = Consume.objects.filter(user=request.user)
    else:
        print("a")

    return render(request, 'calorieTracker/index.html', {'foods': food, 'consumed_foods': consumed_foods})
