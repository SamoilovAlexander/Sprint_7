import requests
from conftest import courier
from data import BASE_URL, ORDERS_URL


class Orders:
    @staticmethod
    def check_list_of_orders(courier):
        return requests.get(f'{BASE_URL}/{ORDERS_URL}?courierId={courier}')
