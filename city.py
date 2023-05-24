import math

class City:
    
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        print(self.name, self.latitude,self.longitude)

    def calculate_distancies(self,citie1,citie2):
        distance = math.sqrt((citie2[0] - citie1[0]) ** 2 + (citie2[1] - citie1[1]) ** 2)
        return distance

    def calculate_adj(cities):
         num_cities = len(cities)
         adj_matriz = [[0] * num_cities for _ in range(num_cities)]

         for i in range(num_cities):
             for j in range(num_cities):
                if i != j:
                  distance = calculate_distancies(cities[i], cities[j])
                  adj_matrix[i][j] = distance

         return adj_matrix    

