import math
from queue import PriorityQueue

class Node:
    
    def __init__(self, number):
        
        self.previous_node = None
        self.number = number
        self.running_cost = 0
        
    def __lt__(self, other):
        
        if self.running_cost != other.running_cost:
            return self.running_cost < other.running_cost
        
        return self.number < other.number

def g(running_cost, from_intersection, to_intersection):
    
    x1, y1 = from_intersection
    x2, y2 = to_intersection

    return int((math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) * 100) + running_cost + 10

def h(intersection, goal_intersection):
    
    x1, y1 = intersection
    x2, y2 = goal_intersection

    return int((math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) * 100)

def f(g, h):
    
    return g + h

def reconstruct(node):
    
    shortest_path = []
    current_node = node
    
    while current_node != None:
        shortest_path.insert(0, current_node.number)
        current_node = current_node.previous_node
    
    return shortest_path
    

def shortest_path(M, start, goal):
    
    frontiers = PriorityQueue()
    best_costs = {start: 0}
    
    start_cost = 0
    start_h_estimate = h(M.intersections[start], M.intersections[goal])
    frontiers.put((f(start_cost, start_h_estimate), Node(start)))
    
    while frontiers:
        f_cost, node = frontiers.get()
        
        if node.number == goal:
            return reconstruct(node)
        
        for neighbour_number in M.roads[node.number]:
            
            current_intersection = M.intersections[node.number]
            neighbour_intersection = M.intersections[neighbour_number]
            neighbour_cost = g(node.running_cost, current_intersection, neighbour_intersection)
            neighbour_h_estimate = h(M.intersections[neighbour_number], M.intersections[goal])
            
            if neighbour_number in best_costs and neighbour_cost >= best_costs[neighbour_number]:
                continue
            
            best_costs[neighbour_number] = neighbour_cost
            
            neighbour_node = Node(neighbour_number)
            neighbour_node.previous_node = node
            neighbour_node.running_cost = neighbour_cost
            
            frontiers.put((f(neighbour_cost, neighbour_h_estimate), neighbour_node))