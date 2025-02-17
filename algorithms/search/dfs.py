def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add all unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return result

# Example usage:
print("Iterative DFS:", dfs_iterative(graph, 'A'))