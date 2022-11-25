import json

import kwargs as kwargs
import requests


username = 'Romashka-LuytikTwo'
password = 'Romashka-Luytik1236Two'


res = requests.get( f"https://petstore.swagger.io/v2/user/login?username={username}&password={password}",
                     headers = {'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))