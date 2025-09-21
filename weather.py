# weather data
import requests

# sending request to get IP location informmation
res = requests.get('https://ipinfo.io/')
data = res.json()

# location of the city
citydata = data['city']
print("Current Location:", citydata)

# passing city name to the URL to get weather data
url = 'https://wttr.in'.format(citydata)
res = requests.get(url)

#printing the weather details of statesboro!
print(res.text)
