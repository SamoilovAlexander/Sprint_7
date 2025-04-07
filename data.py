BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_URL = 'api/v1/courier'
ORDERS_URL = 'api/v1/orders'


import random
import string


def generate_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
# Эти тестовые данные проверяют пункты №№ 1, 4 эндпоинта "Создание заказа"
ORDER_DATA_1 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}

# Эти тестовые данные проверяют пункты №№ 1, 4 эндпоинта "Создание заказа"
ORDER_DATA_2 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Где-то",
    "metroStation": "Московская",
    "phone": "8 223 322 23 32",
    "rentTime": 1,
    "deliveryDate": "2024-12-13",
    "comment": "Иван, ты пьян?",
    "color": ["GREY"]
}

# Эти тестовые данные проверяют пункты №№ 2, 4 эндпоинта "Создание заказа"
ORDER_DATA_3 = {
    "firstName": "Петров",
    "lastName": "Петр",
    "address": "Тута",
    "metroStation": "Питерская",
    "phone": "8 800 555 55 55",
    "rentTime": 2,
    "deliveryDate": "2025-01-22",
    "comment": "Восток - дело тонкое, Петруха",
    "color": ["BLACK", "GREY"]
}

# Эти тестовые данные проверяют пункты №№ 3, 4 эндпоинта "Создание заказа"
ORDER_DATA_4 = {
    "firstName": "Сфинкс",
    "lastName": "Египетский",
    "address": "Далеко",
    "metroStation": "Каирская",
    "phone": " +20 2 25 79 69 48",
    "rentTime": 2,
    "deliveryDate": "2026-01-22",
    "comment": "Я познал вечность",
    "color": []
}
