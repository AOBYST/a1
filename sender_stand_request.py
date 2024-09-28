import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER)

response = post_new_order(data.order_body)

print(response.status_code)


def get_orders_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK)