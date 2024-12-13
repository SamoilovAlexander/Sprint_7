import json

import pytest

from data import ORDER_DATA_1, generate_payload
from methods.creating_courier_methods import NewCourierMethods
from methods.creating_order_methods import NewOrderMethods


@pytest.fixture()
def courier():
    payload = generate_payload()
    NewCourierMethods.create_courier(payload)
    courier_id = NewCourierMethods.login_courier(payload.get('login'), payload.get('password'))
    order_response = NewOrderMethods().create_order(json.dumps(ORDER_DATA_1))
    order_id = NewOrderMethods.getting_order_id(order_response.json()["track"])
    NewOrderMethods.accepting_order(order_id, courier_id)
    yield courier_id
    NewCourierMethods().delete_courier(courier_id)
