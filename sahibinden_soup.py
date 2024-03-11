import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.sahibinden.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')

links = []
for link in soup.find_all('a', class_='classifiedTitle'):
    links.append(link.get('href'))
    print(link.get('href'))

# Save links to JSON file
with open('sahibinden_links.json', 'w') as f:
    json.dump(links, f)
