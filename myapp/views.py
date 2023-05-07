from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.

def index(request):
    if request.method == "POST":
                                # Whatever the user selected only name
        food_consumed = request.POST['food_consumed']
        # for whole food object
        consume = Food.objects.get(name=food_consumed)
        # current user
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods':foods, 'consumed_food': consumed_food})

