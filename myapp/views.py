from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
from django.http import Http404


from django.urls import reverse
from .models import Food, Consume


def index(request):
    if request.method == "POST":
        # use get() instead of [] to avoid KeyError
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            Consume.objects.create(user=user, food_consumed=consume)
            # redirect to the same page to prevent form resubmission
            return redirect(reverse('index'))

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, pk):
    print(pk)
    try:
        consumed_food_id = Consume.objects.get(pk=pk, user=request.user)
    except Consume.DoesNotExist:
        raise Http404("Consume does not exist")

    if request.method == "POST":
        consumed_food_id.delete()
        return redirect('/')
    return render(
        request, 'myapp/delete.html',
        {'consumed_food_id': consumed_food_id})
