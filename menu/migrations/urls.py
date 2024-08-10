from django.urls import path
from .views import PizzaListCreate, PizzaDetail # type: ignore

urlpatterns = [
    path('pizzas/', PizzaListCreate.as_view(), name='pizza-list-create'),
    path('pizzas/<int:pk>/', PizzaDetail.as_view(), name='pizza-detail'),
]
