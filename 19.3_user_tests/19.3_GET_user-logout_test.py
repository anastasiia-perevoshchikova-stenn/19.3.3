import json

import kwargs as kwargs
import requests


res = requests.get( f"https://petstore.swagger.io/v2/user/logout",
                     headers = {'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))