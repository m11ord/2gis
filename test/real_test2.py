import json
import requests

def test_total_count():
 query = {"page" : "1"}
 response = requests.get('https://regions-test.2gis.com/1.0/regions',params=query)
 data = response.json()
 keys = data['items']

 query = {"page": "2"}
 response = requests.get('https://regions-test.2gis.com/1.0/regions', params=query)
 data = response.json()
 keys2 = data['items']

 query = {"page": "3"}
 response = requests.get('https://regions-test.2gis.com/1.0/regions', params=query)
 data = response.json()
 keys3 = data['items']
 total_item = (len(keys) + len(keys2) + len(keys3))
 assert data['total'] == total_item, 'Несоответствие количества регионов'

