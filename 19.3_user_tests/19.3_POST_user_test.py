import json

import kwargs as kwargs
import requests


info = {
  "id": 57595154,
  "username": "LarisaIvanovnaTwo",
  "firstName": "LarisaTwo",
  "lastName": "IvanovnaTwo",
  "email": "LarisaIvanovnaTwo@mail.com",
  "password": "LarisaIvanovna123Two",
  "phone": "+7825646353",
  "userStatus": 0
}


res = requests.post( f"https://petstore.swagger.io/v2/user",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(info, ensure_ascii=False))


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))