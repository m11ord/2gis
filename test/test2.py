import requests

city_ids = []

for page_num in range(1, 5):
    query = {
        "page": page_num,
    }
    data = requests.get('https://regions-test.2gis.com/1.0/regions', params=query).json()
    for i, item in enumerate(data['items']):
        #if (page_num != 1) and (i == 0):
            #print(item)
            #continue
        city_id = item['id']
        city_ids.append(city_id)
print(city_ids, end=' ')
print()
print(len(city_ids))
print(len(set(city_ids)))
assert len(city_ids) == len(set(city_ids))
