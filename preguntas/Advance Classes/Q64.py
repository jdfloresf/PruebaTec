# 64. Write a Python class to implement a graph with methods for 
# adding vertices and edges, and finding the shortest path.

import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))  # For undirected graph

    def dijkstra(self, start, end):
        """Finds the shortest path between two vertices using Dijkstra's 
        algorithm. It uses a priority queue (heap) to keep track of the 
        minimum cost to reach each vertex.
        """
        queue = [(0, start, [])]
        seen = set()
        min_dist = {start: 0}

        while queue:
            (cost, current_vertex, path) = heapq.heappop(queue)
            
            if current_vertex in seen:
                continue
            
            seen.add(current_vertex)
            path = path + [current_vertex]

            if current_vertex == end:
                return (cost, path)

            for (neighbor, weight) in self.vertices[current_vertex]:
                if neighbor in seen:
                    continue
                prev_cost = min_dist.get(neighbor, float('inf'))
                new_cost = cost + weight
                if new_cost < prev_cost:
                    min_dist[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor, path))
        
        return (float('inf'), [])

    def __str__(self):
        return str(self.vertices)


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
print("Graph:", g)
print("Shortest path from A to D:", g.dijkstra('A', 'D'))
