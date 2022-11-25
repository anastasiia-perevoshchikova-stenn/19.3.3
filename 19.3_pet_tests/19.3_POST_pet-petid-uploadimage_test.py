import json
import os
import kwargs as kwargs
import requests
from requests_toolbelt import MultipartEncoder
import base64


petid = 1313151418
pet_photo = 'dog.jpg'


f = open(os.path.join(os.path.dirname(__file__), 'images', pet_photo), 'rb')
data = MultipartEncoder({'file':(pet_photo, f, 'image/jpeg')})
headers = {'accept': 'application/json', 'Content-Type': data.content_type}


base_url = 'https://petstore.swagger.io/v2/pet/'
res = requests.post( base_url + f"{petid}/uploadImage", headers=headers, data=data)


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))