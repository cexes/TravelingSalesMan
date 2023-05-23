import math

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.visited = False

def calculate_distance(city1, city2):
    lat1, lon1 = city1.latitude, city1.longitude
    lat2, lon2 = city2.latitude, city2.longitude
    distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    return distance

def TSP_Nearest_Neighbor(cities, adjacency_matrix):
    initial_city = cities[0]
    initial_city.visited = True
    path = [initial_city]
    total_cost = 0

    while len(path) < len(cities):
        current_city = path[-1]
        nearest_city = None
        min_distance = float('inf')

        for adjacent_city in adjacency_matrix[current_city]:
            if not adjacent_city.visited and adjacency_matrix[current_city][adjacent_city] < min_distance:
                nearest_city = adjacent_city
                min_distance = adjacency_matrix[current_city][adjacent_city]

        path.append(nearest_city)
        nearest_city.visited = True
        total_cost += min_distance

    total_cost += adjacency_matrix[path[-1]][initial_city]
    path.append(initial_city)

    return total_cost, path
