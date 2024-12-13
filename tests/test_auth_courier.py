from methods.auth_courier_methods import AuthCourierMethods


class TestAuthCourier:
    def test_auth_courier(self): # Этот тестовый метод проверяет пункты №№ 1, 2, 6 эндпоинта "Логин курьера"
        auth_courier = AuthCourierMethods.auth_courier()
        assert auth_courier.status_code == 200 and auth_courier.json()['id'] is not None

    def test_auth_courier_without_login(self): # Этот тестовый метод проверяет пункт № 4 эндпоинта "Логин курьера"
        bad_auth_courier = AuthCourierMethods.auth_courier_without_login()
        assert bad_auth_courier.status_code == 400 and bad_auth_courier.json()['message'] == 'Недостаточно данных для входа'

    def test_auth_courier_with_wrong_password(self):  # Этот тестовый метод проверяет пункт № 3 эндпоинта "Логин курьера"
        bad_auth_courier = AuthCourierMethods.auth_courier_with_wrong_password()
        assert bad_auth_courier.status_code == 404 and bad_auth_courier.json()['message'] == 'Учетная запись не найдена'

    def test_auth_courier_with_non_existent_courier(self):  # Этот тестовый метод проверяет пункт № 5 эндпоинта "Логин курьера"
        bad_auth_courier = AuthCourierMethods.auth_courier_with_non_existent_courier()
        assert bad_auth_courier.status_code == 404 and bad_auth_courier.json()['message'] == 'Учетная запись не найдена'
