import requests

url = 'https://regions-test.2gis.com/1.0/regions'
query = {'q': 'ква'}
response = requests.get(url,params=query)
print(response.json())

