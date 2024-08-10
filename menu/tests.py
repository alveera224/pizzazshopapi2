
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Pizza

class PizzaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.pizza_data = {'name': 'Pepperoni', 'ingredients': 'Pepperoni, Cheese', 'price': 10.99}
        self.pizza = Pizza.objects.create(**self.pizza_data)
        self.pizza_detail_url = reverse('pizza-detail', kwargs={'pk': self.pizza.pk})
    
    def test_create_pizza(self):
        response = self.client.post(reverse('pizza-list-create'), self.pizza_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pizza_list(self):
        response = self.client.get(reverse('pizza-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_pizza_detail(self):
        response = self.client.get(self.pizza_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.pizza.name)

    def test_update_pizza(self):
        updated_data = {'name': 'Updated Pizza', 'ingredients': 'Updated ingredients', 'price': 12.99}
        response = self.client.put(self.pizza_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Pizza')

    def test_delete_pizza(self):
        response = self.client.delete(self.pizza_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pizza.objects.count(), 0)

