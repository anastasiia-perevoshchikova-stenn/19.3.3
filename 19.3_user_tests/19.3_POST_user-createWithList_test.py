import json

import kwargs as kwargs
import requests


info = [{
    "id": 123654446,
    "username": "Kalina-MalinaTwo",
    "firstName": "KalinaTwo",
    "lastName": "MalinaTwo",
    "email": "Kalina-MalinaTwo@mail.com",
    "password": "Kalina-Malina1236Two",
    "phone": "+38164641529454",
    "userStatus": 0
  },
{
    "id": 123654447,
    "username": "Romashka-LuytikTwo",
    "firstName": "RomashkaTwo",
    "lastName": "LuytikTwo",
    "email": "Romashka-LuytikTwo@mail.com",
    "password": "Romashka-Luytik1236Two",
    "phone": "+38164641529466",
    "userStatus": 0
  }
]


res = requests.post( f"https://petstore.swagger.io/v2/user/createWithList",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(info, ensure_ascii=False))


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))