""" Handle URL for pizzas app. """

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all pizzas
    path('pizza_list/', views.pizza_list, name='pizza_list'),
    # Show individual pizza
    path('pizza_list/<str:pizza_name>/', views.pizza_page, name='pizza_page'),
]
