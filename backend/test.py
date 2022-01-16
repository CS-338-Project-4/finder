import requests

r = requests.get('https://www.wikidata.org/w/api.php', params={'action':'wbsearchentities', 'search':'abc', 'language':'en', 'format':'json'})

print(r.json())
