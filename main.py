from city import City
import requests

class main:

   cities = [ "Acre" , "Bahia ","Sergipe"]
   lat = []
   lon = []

   for city in cities:
       url = f"https://nominatim.openstreetmap.org/search?format=json&q={city}"
       response = requests.get(url)
       data = response.json()
       latitude = float(data[0]['lat']) 
       lat.append(latitude)
       longitude = float(data[0]['lon'])
       lon.append(longitude)

   for i in range(len(cities)):
       c = City(cities[i],lat[i],lon[i])
  
