import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class WarehouseNetwork:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = np.zeros((num_vertices, num_vertices))

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def plot_graph(self):
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

    def prim_mst(self): # prim's algorithm for MST
        selected = np.zeros(self.num_vertices, dtype=bool)  # track selected vertices
        selected[0] = True  # start from the first vertex
        mst_edges = []
        total_cost = 0

        for _ in range(self.num_vertices - 1):
            min_weight = float("inf")
            u, v = -1, -1

            # Find the minimum weight edge that connects an included vertex to an excluded one
            for i in range(self.num_vertices):
                if selected[i]:
                    for j in range(self.num_vertices):
                        if not selected[j] and self.graph[i][j] > 0 and self.graph[i][j] < min_weight:
                            min_weight = self.graph[i][j]
                            u, v = i, j

            if u != -1 and v != -1:
                selected[v] = True
                mst_edges.append((u, v, min_weight))
                total_cost += min_weight

        # Print and plot MST
        print("Minimum Spanning Tree (MST) Edges:")
        for edge in mst_edges:
            print(f"Warehouse {edge[0]} - Warehouse {edge[1]} (Cost: {edge[2]})")
        print(f"Total Cost of MST: {total_cost}")

        self.plot_mst(mst_edges)

    def plot_mst(self, mst_edges):
        """
        Plots the MST using NetworkX.
        """
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
    num_warehouses = 5  # Change this to let the user specify the number of warehouses
    network = WarehouseNetwork(num_warehouses)

    # Example Edges (Warehouse Connections with Costs)
    edges = [
        (0, 1, 10), (0, 2, 15), (1, 2, 5), (1, 3, 20),
        (2, 3, 30), (2, 4, 8), (3, 4, 25), (0, 4, 40),
        (1, 4, 18), (3, 1, 12)
    ]

    # Adding edges to the network
    for u, v, weight in edges:
        network.add_edge(u, v, weight)

    print("Original Warehouse Network:")
    network.plot_graph()

    print("\nFinding Minimum Spanning Tree (MST):")
    network.prim_mst()
'''
NOT WORKING!!!
def main2():
        num_warehouses = int(input("Enter the number of warehouses (nodes): "))
        network = WarehouseNetwork(num_warehouses)

        num_edges = int(input("Enter the number of connections (edges): "))

        print("Enter each connection in the format: start end weight")
        for _ in range(num_edges):
            u, v, weight = map(int, input().split())
            network.add_edge(u, v, weight)

        print("User-Defined Warehouse Network:")
        network.plot_graph()

        print("\nFinding Minimum Spanning Tree (MST):")
        network.prim_mst()
'''
if __name__ == "__main__":
    main()
    #main2()    #to ask user to input edges
