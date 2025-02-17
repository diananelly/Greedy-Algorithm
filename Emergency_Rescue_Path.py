import heapq


def dijkstra(graph, source):
    # Initialization
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[source] = 0
    # Priority queue storing (distance, node)
    heap = [(0, source)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        # Skip if a shorter path to u has been found
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            alt = dist[u] + weight
        if alt < dist[v]:
            dist[v] = alt
        prev[v] = u
        heapq.heappush(heap, (alt, v))
    return dist, prev


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'Baptist': [('Jackson West', 3), ('Palmetto', 4)],
        'Jackson West': [('Baptist', 3), ('Palmetto', 1), ('D', 7)],
        'Palmetto': [('A', 4), ('B', 1), ('E', 3)],
        'Kendall': [('B', 7), ('F', 1)],
        'St. Nicholas': [('C', 3), ('D', 2), ('F', 5)]
    }
    source = 'A'
    dist, prev = dijkstra(graph, source)
    # Print the results
    print("Shortest distances from the source to each node:")
    for vertex in dist:
        print(f"Distance from {source} to {vertex} is {dist[vertex]}")
    # Reconstruct the shortest path from source to target
    target = 'C'
    path = []
    current = target
    while current:
        path.insert(0, current)
        current = prev[current]
    print(f"Shortest path from {source} to {target}: {' -> '.join(path)}")
