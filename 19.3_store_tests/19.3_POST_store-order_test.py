import json

import kwargs as kwargs
import requests


info = {
  "id": 9,
  "petId": 1313151418,
  "quantity": 1,
  "shipDate": "2022-11-20T10:49:00.808Z",
  "status": "placed",
  "complete": True
}

res = requests.post( f"https://petstore.swagger.io/v2/store/order",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))