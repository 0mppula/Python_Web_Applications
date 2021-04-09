from django.shortcuts import render

from pizzas.models import Pizza, Topping


def index(request):
    """ The homepage for pizzas app. """
    return render(request, 'pizzas/index.html')

def pizza_list(request):
    """ Show all pizzas on the page. """
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza_page(request, pizza_name):
    """ Show a specific pizza and its toppings on the page. """
    pizzas = Pizza.objects.order_by('date_added')
    for p in pizzas:
        if p.name == pizza_name:
            pizza = p 
            break

    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

