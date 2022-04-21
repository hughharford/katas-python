# Chris Westerman
# day 3, le wagon

import requests

# # the very basics
# url = 'https://cat-fact.herokuapp.com/facts/'
# response = requests.get(url)

# print(type(response))
# print(dir(response))

# print(response.content)
# b' at the start indicates bytestring

# print(response.json())
# print(type(response.json()))

# javascript: 'https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&callback=mycallback'
# to get json:
'https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=JSON'
# add data command to see more:
our_url_string = 'https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=JSON&jscmd=data'

base_url = 'https://openlibrary.org/api/books'
# ISBN:0451526538
ISBN = '0451526538'
key = f'ISBN:{ISBN}'
params = {'bibkeys': key,
       'format': 'json',
       'jscmd': 'data'
       }

response = requests.get(base_url, params=params)
print(response.json()[key]['title'])
