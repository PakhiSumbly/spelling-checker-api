import requests

url = 'http://127.0.0.1:5002/correct'

data = {'text': "jam is coolder nowp"}                 #"she is wayyy too tally"  #"It's bwwn so long"   "birds flyy high"  #"jam is coolder nowp"

response = requests.post(url, json=data)

print(response.json())
