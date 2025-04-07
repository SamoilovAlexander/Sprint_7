import json

import pytest


from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4
from methods.creating_order_methods import NewOrderMethods


class TestCreateOrder:

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4])
    def test_create_order(self, order_data):
        new_order = NewOrderMethods.create_order(json.dumps(order_data))
        print(new_order.json()['track'])
        assert new_order.status_code == 201 and new_order.json()['track'] is not None
