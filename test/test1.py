import requests
import json

payload = {"country_code": "ua"}
r = requests.get("https://regions-test.2gis.com/1.0/regions", params=payload)
data = r.json()
#for i in data.get('items'):
#     assert (i.get("name")) == 'Днепр'

for i in data['items']:
    #print(i.get('country'))
    print(i['country'],i['code'])
    assert (i['country']['name']) == 'Украина' , 'Несоответствие регионов'
#for item in i['country']:
    #print(item)

#print(response.request)
#print(response.status_code)
#print(response.headers)
#print(response.content)
#print(response.text)
#print(r.json())

#сколько раз повторяется значение словаря
 #for i in data['items']:
  #K = 'Днепр'
  #res = 0
 #for key in i:
  #if i[key] == K:
   #res = res + 1
 #print("Frequency of K is : " + str(res))
 #print(i)