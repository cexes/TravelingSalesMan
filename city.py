import math

class City:
    
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def calculate_distancies(self,lat1,lon1,lat2,lon2):
        distance = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) 
        return distance

    def TSP_Narest_Neighbor(self,cities,matriz):
        num_cit = len(cidad)
        visited = [false] * num_cit
        init_city = 0 
        visted[init_city] = True
        total = 0


 


    def calculate_adj(cities):
         num_cities = len(cities)
         adj_matriz = [[0] * num_cities for _ in range(num_cities)]

         for i in range(num_cities):
             for j in range(num_cities):
                if i != j:
                  distance = calculate_distancies(cities[i], cities[j])
                  adj_matrix[i][j] = distance

         return adj_matrix    

