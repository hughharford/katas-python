import requests

from bs4 import BeautifulSoup

url = 'https://www.lewagon.com/london'

response = requests.get(url)

# can use XML parser too if need be:
soup = BeautifulSoup(response.content, 'html.parser')
# print(type(soup))
# print(soup)

# NOTES:
# will almost always be looking to find Classes
# just need to find the right one, as classes repeatedly


title = soup.title.string
# soup.find('h1')
# soup.find_all('a')

# print(soup.find_all('div',class_='item-content'))

# not sure how to chain through to get the specific data
#### HOW TO:
    # get the overall data, then chain for through until you get what you want

raw = soup.find_all('div',class_='item-content')
# print(raw)

for detail in raw:
    name = detail.find_all('span',class_='full-name')
    print(name)
