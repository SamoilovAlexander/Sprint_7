from data import generate_payload
from methods.creating_courier_methods import NewCourierMethods


class TestCreateCourier:
    def test_create_courier(self): # Этот тестовый метод проверяет пункты №№ 1, 4, 5 эндпоинта "Создание курьера"
        payload = generate_payload()
        new_courier = NewCourierMethods.create_courier(payload)
        assert new_courier.status_code == 201 and new_courier.json() == {'ok':True}

    def test_create_the_same_couriers(self): # Этот тестовый метод проверяет пункты №№ 2, 7 эндпоинта "Создание курьера"
        the_same_courier = NewCourierMethods.create_the_same_couriers()
        assert the_same_courier.status_code == 409 and the_same_courier.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    def test_create_courier_without_login(self): # Этот тестовый метод проверяет пункты №№ 3, 6 эндпоинта "Создание курьера"
        courier_without_login = NewCourierMethods.create_courier_without_login()
        assert courier_without_login.status_code == 400 and courier_without_login.json()['message'] == 'Недостаточно данных для создания учетной записи'

    def test_create_courier_without_password(self): # Этот тестовый метод проверяет пункты №№ 3, 6 эндпоинта "Создание курьера"
        courier_without_password = NewCourierMethods.create_courier_without_password()
        assert courier_without_password.status_code == 400 and courier_without_password.json()['message'] == 'Недостаточно данных для создания учетной записи'
