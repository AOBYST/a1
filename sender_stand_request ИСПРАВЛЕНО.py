import configuration
import requests
import data
def create_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body)
def get_orders_track (track_number):
    get_order_url =f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
def test_create_new_order():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    print(track_number)
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print(order_data)

