import json

import kwargs as kwargs
import requests


Id = 1313151418
name = 'LillyBunnieeeCutie'
status='pending'


res = requests.post( f"https://petstore.swagger.io/v2/pet/{Id}",
                     headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                     data= f"name={name}&status={status}")

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))