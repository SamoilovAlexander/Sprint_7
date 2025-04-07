from methods.check_list_of_order_methods import Orders
from conftest import courier


class TestCheckListOfOrders:
    def test_check_orders(self, courier): # Этот тестовый метод проверяет эндпоинт "Список заказов"
        response = Orders.check_list_of_orders(courier)
        assert response is not None
