import math
import requests

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.visited = False

    def calculate_distance(self, other_city):
        lat1 = self.latitude
        lon1 = self.longitude
        lat2 = other_city.latitude
        lon2 = other_city.longitude
        distance = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
        return distance

def TSP_Nearest_Neighbor(cities, adjacency_matrix):
    start_city = cities[0]
    current_city = start_city
    current_city.visited = True
    path = [current_city]
    total_cost = 0

    while len(path) < len(cities):
        nearest_city = None
        min_distance = float('inf')

        for adjacent_city in adjacency_matrix[current_city]:
            if not adjacent_city.visited and adjacency_matrix[current_city][adjacent_city] < min_distance:
                nearest_city = adjacent_city
                min_distance = adjacency_matrix[current_city][adjacent_city]

        path.append(nearest_city)
        nearest_city.visited = True
        total_cost += min_distance
        current_city = nearest_city

    total_cost += adjacency_matrix[path[-1]][start_city]
    path.append(start_city)

    return total_cost, path

# Obtenha as coordenadas das cidades usando a API OpenStreetMap (neste caso, as coordenadas são fornecidas manualmente)
cities = [
    City("Itaquera", -23.5427, -46.4731),
    City("Bahia", -12.9711, -38.5108),
    City("Tatuapé", -23.5389, -46.5737)
]

# Calcula a matriz de adjacências
adjacency_matrix = {}

for city in cities:
    distances = {}
    for other_city in cities:
        if city != other_city:
            distance = city.calculate_distance(other_city)
            distances[other_city] = distance
    adjacency_matrix[city] = distances

# Execute o algoritmo TSP - Vizinho Mais Próximo
cost, path = TSP_Nearest_Neighbor(cities, adjacency_matrix)

# Imprima o menor custo e o melhor caminho encontrado
print("Menor custo:", cost)
print("Melhor caminho:")
for city in path:
    print(city.name)
