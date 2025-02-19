import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import heapq  # import heapq for the priority queue

class WarehouseNetwork:
    def __init__(self, num_vertices):
        # initialize graph with given number of vertices
        self.num_vertices = num_vertices
        self.graph = np.zeros((num_vertices, num_vertices))

    def add_edge(self, u, v, weight):
        # add an edge to the graph
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def plot_graph(self):
        # plot the entire warehouse network
        G = nx.Graph()
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j, weight=self.graph[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, "weight")

        plt.figure(figsize=(8, 6))
        plt.title("Whole Warehouse Network")
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=700, font_size=10, edge_color="gray")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def prim_mst(self):
        # implement Prim's algorithm to find the minimum spanning tree (MST)
        selected = np.zeros(self.num_vertices, dtype=bool)
        selected[0] = True
        mst_edges = []
        total_cost = 0

        pq = []
        for j in range(1, self.num_vertices):
            if self.graph[0][j] > 0:
                heapq.heappush(pq, (self.graph[0][j], 0, j))

        while pq:
            weight, u, v = heapq.heappop(pq)

            if selected[v]:
                continue

            selected[v] = True
            mst_edges.append((u, v, weight))
            total_cost += weight

            for w in range(self.num_vertices):
                if not selected[w] and self.graph[v][w] > 0:
                    heapq.heappush(pq, (self.graph[v][w], v, w))

        print("Minimum Spanning Tree (MST) Edges:")
        for edge in mst_edges:
            print(f"Warehouse {edge[0]} - Warehouse {edge[1]} (Cost: {edge[2]})")
        print(f"Total Cost of MST: {total_cost}")

        self.plot_mst(mst_edges)

    def plot_mst(self, mst_edges):
        # plot the minimum spanning tree of the warehouse network
        G = nx.Graph()
        for u, v, weight in mst_edges:
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, "weight")

        plt.figure(figsize=(8, 6))
        plt.title("MST Warehouse Network")
        nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=700, font_size=10, edge_color="blue")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


def main():
    # create a hardcoded example warehouse network
    num_warehouses = 5
    network = WarehouseNetwork(num_warehouses)

    edges = [
        (0, 1, 10), (0, 2, 15), (1, 2, 5), (1, 3, 20),
        (2, 3, 30), (2, 4, 8), (3, 4, 25), (0, 4, 40),
        (1, 4, 18), (3, 1, 12)
    ]

    for u, v, weight in edges:
        network.add_edge(u, v, weight)

    print("Original Warehouse Network:")
    network.plot_graph()

    print("\nFinding Minimum Spanning Tree (MST):")
    network.prim_mst()


def main_user_input():
    # prompt user to input vertices and edges for the warehouse network
    # due to the nature of this assignment, this feature is very buggy, input must be exact
    # vertexes start at index 0
    # edge might overwrite if given duplicate edge
    num_vertices = int(input("Enter the number of vertices: "))
    network = WarehouseNetwork(num_vertices)

    num_edges = int(input("Enter the number of edges: "))
    print("Provide edges in the format: vertex1 vertex2 weight")

    for _ in range(num_edges):
        u, v, weight = map(int, input("Edge (u v weight): ").split())
        network.add_edge(u, v, weight)

    print("User Inputted Warehouse Network:")
    network.plot_graph()

    print("\nFinding Minimum Spanning Tree (MST):")
    network.prim_mst()


if __name__ == "__main__":
    # determine if the user wants a hardcoded or custom input graph
    choice = input("Do you want to use the hardcoded graph or input your own? (h/u): ").lower()
    if choice == 'h':
        main()
    elif choice == 'u':
        main_user_input()
    else:
        print("Invalid choice. Please restart and select 'h' or 'u'.")
