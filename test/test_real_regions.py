from pprint import pprint

import pytest
import requests
import json


@pytest.mark.parametrize(
    "query, expected_country", (
            ({"country_code": "kz"}, "Казахстан"),
            ({"country_code": "ru"}, "Россия"),
    )
)
def test_region1(
        query,
        expected_country,
):
    url = 'https://regions-test.2gis.com/1.0/regions'
    response = requests.get(url, params=query)
    data = response.json()
    pprint(data)
    for i in data['items']:
        actual_country = i['country']['name']
        assert actual_country == expected_country, \
            f'Несоответствие регионов. Ожидаемый регион {expected_country}, фактический регион {actual_country}'


def test_region():
    url = 'https://regions-test.2gis.com/1.0/regions'
    query = {"country_code": "ua"}
    response = requests.get(url, params=query)
    data = response.json()
    for i in data['items']:
        assert (i['country']['name']) == 'Украина', 'Несоответствие регионов'
    # _______________
    query = {"country_code": "ru"}
    response = requests.get(url, params=query)
    data = response.json()
    for i in data['items']:
        assert (i['country']['name']) == 'Россия', 'Несоответствие регионов'
    # _______________
    query = {"country_code": "cz"}
    response = requests.get(url, params=query)
    data = response.json()
    for i in data['items']:
        assert (i['country']['name']) == 'Чехия', 'Несоответствие регионов'
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

# test_region()
