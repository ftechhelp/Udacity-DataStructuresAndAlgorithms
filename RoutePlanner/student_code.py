import math

class City:
    
    def __init__(self, intersection, number, roads):
        self.coordinates = intersection
        self.city_number = number
        self.connected_city_numbers = roads

def get_cost(start_city, end_city):
    x1, y1 = start_city.coordinates
    x2, y2 = end_city.coordinates
    
    return int((math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) * 100)
    

def shortest_path(M, start, goal):
    start_city = City(M.intersections[start], start, M.roads[start])
    frontiers = [start_city]
    explored = set()
    
    print(start_city)