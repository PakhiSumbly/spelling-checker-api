import requests

url = 'http://127.0.0.1:5002/correct'

data = {'text': "It's bwwn so long"}

response = requests.post(url, json=data)

print(response.json())
