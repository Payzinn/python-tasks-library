import requests
import json

request = requests.get('https://swapi.dev/api/people/3')
data = json.loads(request.text)
data['name'] = 'Nikita'

with open('character.json', 'w') as json_file:
    json.dump(data, json_file, indent = 4)

with open('home.json', 'w') as json_file:
    json.dump(data['homeworld'], json_file)