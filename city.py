import requests
"""
Módulo que contém a definição da classe City.
"""

class City:
    """
    Classe que representa uma cidade.
    """

    def __init__(self, citys):
        """
        Inicializa uma instância da classe City.

        Args:
            city (str): O nome da cidade.
            latitude (float): A latitude da cidade.
            longitude (float): A longitude da cidade.
        """
        self.citys = citys
        print(self.citys)

    def get_longitude_latitude(self):
        i = 0
        while i < len(self.citys):
          url =f"https://nominatim.openstreetmap.org/search?format=json&q={self.citys[i]}"
          response = requests.get(url)
          data = response.json()
          latitude = data[0]['lat']
          longitude = data[0]['lon']
          print(self.citys[i],'latidude: ',latitude," ",'longitude: ', longitude)
          i +=1
way = ['acre', 'bahia','amazonas']
city = City(way)        
print(city.get_longitude_latitude())
