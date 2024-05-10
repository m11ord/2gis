import requests
import json



url = 'https://regions-test.2gis.com/1.0/regions'
query = {'country_code': 'ru'}
data = response = requests.get(url,params=query).json()
for i in data['items']:
 p1 = i['name']
 print(p1, end='; ')

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