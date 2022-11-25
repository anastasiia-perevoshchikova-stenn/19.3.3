import json

import kwargs as kwargs
import requests


Id = 1313151418


res = requests.delete( f"https://petstore.swagger.io/v2/pet/{Id}",
                       headers = {'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))