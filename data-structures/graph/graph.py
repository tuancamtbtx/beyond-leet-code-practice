class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a new vertex with an empty list of neighbors
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1, directed=False):
        # Add an edge from vertex1 to vertex2 with an optional weight
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
            if not directed:
                # If the graph is undirected, add an edge in the opposite direction
                self.adjacency_list[vertex2].append((vertex1, weight))

    def display(self):
        # Display the graph as an adjacency list
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {neighbors}")

# Example usage
if __name__ == "__main__":
    graph = Graph()
    
    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    
    # Add edges
    graph.add_edge("A", "B", weight=2)
    graph.add_edge("A", "C", weight=3)
    graph.add_edge("B", "C", weight=1, directed=True)
    
    # Display the graph
    graph.display()