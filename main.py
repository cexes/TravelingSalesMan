from city import City
import requests

class main:

   cities = [ "Acre" , "Bahia ","Sergipe"]


   for city in cities:
       url = f"https://nominatim.openstreetmap.org/search?format=json&q={city}"
       response = requests.get(url)
       data = response.json()
       latitude = data[0]['lat'] 
       longitude = data[0]['lon']

   for i in range(len(cities)):
       city = City(cities[i],latitude,longitude)        
