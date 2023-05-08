from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.


from django.urls import reverse
from .models import Food, Consume

def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')  # use get() instead of [] to avoid KeyError
        if food_consumed:
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            Consume.objects.create(user=user, food_consumed=consume)
            # redirect to the same page to prevent form resubmission
            return redirect(reverse('index'))

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods':foods, 'consumed_food': consumed_food})
