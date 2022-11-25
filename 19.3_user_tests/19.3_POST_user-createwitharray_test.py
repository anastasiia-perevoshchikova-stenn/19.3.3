import json

import kwargs as kwargs
import requests


info = [{
    "id": 646411,
    "username": "IndiraGhandiSuperStarThree",
    "firstName": "IndiraThree",
    "lastName": "GhandiThree",
    "email": "IndiraGhandiSuperStarThree@mail.com",
    "password": "IndiraGhandi123Three",
    "phone": "+3810646412588",
    "userStatus": 0
  },
    {
        "id": 646422,
        "username": "IndiraGhandiSuperStarFour",
        "firstName": "IndiraFour",
        "lastName": "GhandiFour",
        "email": "IndiraGhandiSuperStarFour@mail.com",
        "password": "IndiraGhandi123Four",
        "phone": "+3810646412589",
        "userStatus": 0
    }
]


res = requests.post( f"https://petstore.swagger.io/v2/user/createWithArray",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(info, ensure_ascii=False))


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))