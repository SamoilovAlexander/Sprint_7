import requests

from data import BASE_URL, COURIER_URL, generate_payload


class NewCourierMethods:
    @staticmethod
    def create_courier(payload):
        return requests.post(f'{BASE_URL}/{COURIER_URL}', data=payload)

    @staticmethod
    def create_the_same_couriers():
        payload = generate_payload()
        requests.post(f'{BASE_URL}/{COURIER_URL}', data=payload)
        return requests.post(f'{BASE_URL}/{COURIER_URL}', data=payload)

    @staticmethod
    def create_courier_without_login():
        payload = generate_payload()
        return requests.post(f'{BASE_URL}/{COURIER_URL}',
                             data={'password': payload.get('password'), 'firstName': payload.get('first_name')})

    @staticmethod
    def create_courier_without_password():
        payload = generate_payload()
        return requests.post(f'{BASE_URL}/{COURIER_URL}',
                             data={'login': payload.get('login'), 'firstName': payload.get('first_name')})

    @staticmethod
    def login_courier(login, password):
        response = requests.post(f'{BASE_URL}/{COURIER_URL}/login', data={'login': login, 'password': password})
        return response.json()['id']

    @staticmethod
    def delete_courier(id):
        requests.delete(f'{BASE_URL}/{COURIER_URL}/{id}')
