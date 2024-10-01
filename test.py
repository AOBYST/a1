import data
from sender_stand_request import create_order, get_orders_track


def test_create_new_order():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    print(track_number)
    order_response = get_orders_track(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print(order_data)