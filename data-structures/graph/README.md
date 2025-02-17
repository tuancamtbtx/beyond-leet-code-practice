A graph is a data structure that consists of a set of nodes (or vertices) and a set of edges that connect pairs of nodes. Graphs can be used to represent various real-world systems such as computer networks, social networks, transportation systems, and more.

### Types of Graphs

- **Directed vs. Undirected Graphs**: In a directed graph, edges have a direction, indicating a one-way relationship between nodes. In an undirected graph, edges have no direction, indicating a two-way relationship.

- **Weighted vs. Unweighted Graphs**: In a weighted graph, edges have weights representing costs, distances, or other metrics. In an unweighted graph, all edges are considered equal.

### Graph Representation

Graphs can be represented in several ways, with the most common being:

1. **Adjacency Matrix**: A 2D array where the cell at row `i` and column `j` indicates the presence (and possibly the weight) of an edge between node `i` and node `j`.

2. **Adjacency List**: A list where each element represents a node and contains a list of adjacent nodes (and possibly weights).

### Example: Graph Representation in Python

Let's implement a simple graph using an adjacency list in Python:

```python
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
```

### Explanation:

- **Graph Class**: We define a `Graph` class with an `adjacency_list` attribute to store the graph.

- **add_vertex Method**: Adds a vertex to the graph by initializing an empty list for it in the adjacency list.

- **add_edge Method**: Adds an edge between two vertices. It optionally takes a weight and a `directed` flag to indicate whether the graph is directed.

- **display Method**: Prints the graph's adjacency list, showing each vertex and its adjacent vertices with weights.

This implementation provides a basic framework for working with graphs in Python. You can extend it with more advanced features, such as methods for graph traversal (e.g., depth-first search, breadth-first search), finding shortest paths, detecting cycles, etc.