import requests
import json

request = requests.get('https://swapi.dev/api/films')
data = json.loads(request.text)

# with open('films.json', 'w') as films:
#     json.dump(data, films, indent = 4)

opening = (data['results'][0]['opening_crawl'])

with open('crawl.txt', 'w') as crawl:
    crawl.write(opening)

with open('crawl.txt', 'r') as crawl:
    data = json.load(crawl)