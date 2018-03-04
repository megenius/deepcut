import requests

r = requests.get('http://localhost:5000/?q={}'.format("ทดสอบการตัดคำภาษาไทย"))
print(r.json()['data'])