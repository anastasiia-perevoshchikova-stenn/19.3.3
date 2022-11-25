import json

import kwargs as kwargs
import requests


username = 'Romashka-LuytikTwo'


info = {
  "id": 123654447,
  "username": "Romashka-LuytikTwo",
  "firstName": "RomashkaTwoThreeFour",
  "lastName": "LuytikTwo",
  "email": "Romashka-LuytikTwo@mail.com",
  "password": "Romashka-Luytik1236Two",
  "phone": "+38164641529466",
  "userStatus": 0
}


res = requests.put( f"https://petstore.swagger.io/v2/user/{username}",
                    headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(info, ensure_ascii=False))


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))