# Made to test azuresearch

import requests
from pprint import pprint as pp

endpoint = 'https://shellfishsearch.search.windows.net/indexes/documentdb-index/docs?api-version=2017-11-11&$count=true&queryType=full&$select=*&serachField=Names&search="Doe, Jane"'#Doe"'#,Jane 52"' # 1"'
api_key = '0B16609C8404A9314BAEB433A64F0276'
headers = {'api-key': api_key, 'Accept': 'application/json'}

r = requests.get(endpoint, headers=headers)

print(r.status_code)


test = 'https://shellfishsearch.search.windows.net'

#r = requests.get(test, headers=headers)

