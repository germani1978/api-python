import requests
#https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#https://pypi.org/project/requests/

#1XX Hold On
#2XX Here You Go
#3XX Go Away
#4XX You Screwed Up
#5XX I Screwed Up

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

latitud = data['iss_position']['latitude']
longitud = data['iss_position']['longitude']
iss_position = (longitud, latitud)
print(iss_position)



