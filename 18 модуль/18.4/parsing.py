import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3')
#print(my_req.text)
# with open('google.html', 'w', encoding='utf8') as file_html:
#     file_html.write(my_req.text)
data = json.loads(my_req.text) #десерилизация json
data['name'] = 'nikita'
#print(data['name'])

with open('my.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, indent = 4) #серелизация json


with open('my.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file) #десерилизация json, если буквы s в load нет, значит мы работаем с файлом

print(data)# load лучше использовать после десерилизации json