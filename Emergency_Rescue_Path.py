import heapq
import matplotlib.pyplot as plt
import networkx as nx


class EmergencyRescue:
    def __init__(self, num_locations):
        self.num_locations = num_locations
        self.graph = {i: {} for i in range(num_locations)}  # adjacency list

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # undirected graph

    def dijkstra(self, start, target):
        # finds the shortest path from start to target using dijkstra's algorithm
        queue = [(0, start)]  # min-heap priority queue
        distances = {i: float('inf') for i in range(self.num_locations)}
        previous_nodes = {i: None for i in range(self.num_locations)}
        distances[start] = 0

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == target:
                break

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        # reconstructs the shortest path
        path = []
        current_node = target
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]

        return path[::-1], distances[target]

    def plot_graph(self):
        # plots the city road network
        G = nx.Graph()
        for u in self.graph:
            for v, weight in self.graph[u].items():
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, "weight")

        plt.figure(figsize=(8, 6))
        plt.title("City Road Network")
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=700, font_size=10, edge_color="gray")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


def main():
    # creates a new emergency rescue instance with 5 locations
    rescue_system = EmergencyRescue(5)

    # adds edges to the graph (roads between locations)
    rescue_system.add_edge(0, 1, 15)
    rescue_system.add_edge(0, 2, 25)
    rescue_system.add_edge(0, 3, 10)
    rescue_system.add_edge(1, 3, 20)
    rescue_system.add_edge(1, 4, 30)
    rescue_system.add_edge(2, 3, 5)
    rescue_system.add_edge(2, 4, 15)
    rescue_system.add_edge(3, 4, 10)
    rescue_system.add_edge(3, 1, 25)
    rescue_system.add_edge(4, 2, 20)

    # plots the city road network
    rescue_system.plot_graph()

    # use case 1: find the fastest route from disaster zone (0) to hospital a (1)
    print("Finding fastest route from Disaster Zone (0) to Hospital A (1):")
    path, total_time = rescue_system.dijkstra(0, 1)
    print("Fastest path:", path)
    print("Total travel time:", total_time)

    # use case 2: find the fastest route from disaster zone (0) to hospital b (2)
    print("\nFinding fastest route from Disaster Zone (0) to Hospital B (2):")
    path, total_time = rescue_system.dijkstra(0, 2)
    print("Fastest path:", path)
    print("Total travel time:", total_time)

    # use case 3: find the fastest route from disaster zone (0) to intersection d (4)
    print("\nFinding fastest route from Disaster Zone (0) to Intersection D (4):")
    path, total_time = rescue_system.dijkstra(0, 4)
    print("Fastest path:", path)
    print("Total travel time:", total_time)


if __name__ == "__main__":
    main()
