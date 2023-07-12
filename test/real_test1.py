import requests
import json

def test_region():
 url = 'https://regions-test.2gis.com/1.0/regions'
 query = {"country_code": "ua"}
 response = requests.get(url,params=query)
 data = response.json()
 for i in data['items']:
    assert (i['country']['name']) == 'Украина' , 'Несоответствие регионов'
#_______________
 query = {"country_code": "ru"}
 response = requests.get(url,params=query)
 data = response.json()
 for i in data['items']:
    assert (i['country']['name']) == 'Россия' , 'Несоответствие регионов'
# _______________
 query = {"country_code": "cz"}
 response = requests.get(url,params=query)
 data = response.json()
 for i in data['items']:
    assert (i['country']['name']) == 'Чехия' , 'Несоответствие регионов'
# _______________
 query = {"country_code": "kz"}
 response = requests.get(url, params=query)
 data = response.json()
 for i in data['items']:
    assert (i['country']['name']) == 'Казахстан', 'Несоответствие регионов'
# _______________
 query = {"country_code": "kg"}
 response = requests.get(url, params=query)
 data = response.json()
 for i in data['items']:
    assert (i['country']['name']) == 'Кыргызстан', 'Несоответствие регионов'

test_region()