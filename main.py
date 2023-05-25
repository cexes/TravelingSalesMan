from city import City
import requests

class main:

   cities = [ "Itaquera" , "Bahia ","Tatuape"]
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

   for i in range(len(cities) -1):
       c = City( cities[i], lat[i], lon[i]) 
       distance =  c.calculate_distancies (lat[i] , lon[i], lat[i+1], lon[i+1])
       print("Distância entre", c.name, "e", cities[i+1], ":", distance)
