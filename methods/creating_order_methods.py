import requests
from data import BASE_URL, ORDERS_URL


class NewOrderMethods:
    @staticmethod
    def create_order(payload):
        return requests.post(f'{BASE_URL}/{ORDERS_URL}', data = payload)

    @staticmethod
    def getting_order_id(track):
        response = requests.get(f'{BASE_URL}/{ORDERS_URL}/track?t={track}')
        return response.json()["order"]["id"]

    @staticmethod
    def accepting_order(order_id, courier_id):
        return requests.put(f'{BASE_URL}/{ORDERS_URL}/accept/{order_id}?courierId={courier_id}')
