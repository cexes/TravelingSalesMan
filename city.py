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

def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={city_name}"
    response = requests.get(url)
    data = response.json()
    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return latitude, longitude
    else:
        return None, None

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

def TSP_Minimum_Spanning_Tree(cities, adjacency_matrix):
    start_city = cities[0]
    start_city.visited = True
    visited_cities = [start_city]
    total_cost = 0
    tree_edges = []

    while len(visited_cities) < len(cities):
        min_distance = float('inf')
        min_edge = None

        for source_city in visited_cities:
            for destination_city in cities:
                if destination_city not in visited_cities:
                    distance = adjacency_matrix[source_city][destination_city]
                    if distance < min_distance:
                        min_distance = distance
                        min_edge = (source_city, destination_city)

        source, destination = min_edge
        visited_cities.append(destination)
        total_cost += min_distance
        tree_edges.append(min_edge)

    return total_cost, tree_edges

# Exemplo de cidades com coordenadas manualmente definidas
city_names = ["Itaquera,","Bahia","Tatuape"]
# Obter as coordenadas das cidades usando a API do OpenStreetMap
cities = []
for city_name in city_names:
    latitude, longitude = get_coordinates(city_name)
    city = City(city_name, latitude, longitude)
    cities.append(city)

# Calcular a matriz de adjacências usando a distância Euclidiana
adjacency_matrix = {}
for city in cities:
    adjacency_matrix[city] = {}
    for other_city in cities:
        if city != other_city:
            distance = city.calculate_distance(other_city)
            adjacency_matrix[city][other_city] = distance

# Execute o algoritmo TSP - Vizinho mais Próximo
cost_nn, path_nn = TSP_Nearest_Neighbor(cities, adjacency_matrix)

# Imprima o menor custo e o melhor caminho encontrado usando o Vizinho mais Próximo
print("Custo (Vizinho mais Próximo):", cost_nn)
print("Melhor Caminho (Vizinho mais Próximo):")
for city in path_nn:
    print(city.name)

# Execute o algoritmo TSP - Árvore Geradora Mínima
cost_mst, tree_edges_mst = TSP_Minimum_Spanning_Tree(cities, adjacency_matrix)

# Imprima o custo e a árvore encontrada usando a Árvore Geradora Mínima
print("Custo (Árvore Geradora Mínima):", cost_mst)
print("Árvore (Árvore Geradora Mínima):")
for edge in tree_edges_mst:
    source_city, destination_city = edge
    print(source_city.name, "->", destination_city.name)
