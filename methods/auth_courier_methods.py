import requests
from data import BASE_URL, COURIER_URL, generate_payload


def create_courier(payload):
    requests.post(f'{BASE_URL}/{COURIER_URL}', data=payload)


class AuthCourierMethods:
    @staticmethod
    def auth_courier():
        payload = generate_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}/{COURIER_URL}/login',
                                      data={'login': payload.get('login'), 'password': payload.get('password')})

    @staticmethod
    def auth_courier_without_login():
        payload = generate_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}/{COURIER_URL}/login', data={'password': payload.get('password')})

    @staticmethod
    def auth_courier_with_wrong_password():
        payload = generate_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}/{COURIER_URL}/login', data={'login': payload.get('login'), 'password': 'password'})

    @staticmethod
    def auth_courier_with_non_existent_courier():
        payload = generate_payload()
        return requests.post(f'{BASE_URL}/{COURIER_URL}/login', data={'login': payload.get('login'), 'password': payload.get('password')})
