import json

import kwargs as kwargs
import requests


username = 'LarisaIvanovnaTwo'


res = requests.delete( f"https://petstore.swagger.io/v2/user/{username}",
                     headers = {'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))