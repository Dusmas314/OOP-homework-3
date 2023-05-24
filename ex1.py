import requests

r = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json').json()
name = ''
intell = 0
for superhero in r:
    if superhero['name'] == 'Thanos' or superhero['name'] == 'Captain America' or superhero['name'] == 'Hulk':
        if superhero['powerstats']['intelligence'] > intell:
            intell = superhero['powerstats']['intelligence']
            name = superhero['name']
print(name)
