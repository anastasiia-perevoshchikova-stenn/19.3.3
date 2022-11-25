import json

import kwargs as kwargs
import requests


orderId = 9


res = requests.delete( f"https://petstore.swagger.io/v2/store/order/{orderId}",
                       headers = {'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))