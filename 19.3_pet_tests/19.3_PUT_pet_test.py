import json

import kwargs as kwargs
import requests


info = {
  "id": 1313151418,
  "category": {
    "id": 5,
    "name": "Fly"
  },
  "name": "Mukha-Fly",
  "photoUrls": [
    "https://vsezhivoe.ru/wp-content/uploads/2017/11/zayac.jpg"
  ],
  "tags": [
    {
      "id": 5,
      "name": "Fly"
    }
  ],
  "status": "available"
}


res = requests.put( f"https://petstore.swagger.io/v2/pet",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))