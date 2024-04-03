import networkx as nx

# Function to find the minimum spanning tree of a graph
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

# Main function
def main():
    # Create the bigger graph with weights
    bigger_graph = nx.Graph()
    bigger_graph.add_weighted_edges_from([
        ('A', 'B', 2),
        ('A', 'C', 3),
        ('B', 'C', 4),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('C', 'E', 6),
        ('D', 'E', 7)
    ])
    
    print("Input the subgraph (list of nodes):")
    subgraph_nodes = input().split()

    # Extract subgraph from the bigger graph
    subgraph = bigger_graph.subgraph(subgraph_nodes)
    
    print("\nMinimum Spanning Tree Path of the subgraph:")
    mst = minimum_spanning_tree(subgraph)
    print("Path:", list(nx.dfs_edges(mst)))

if __name__ == "__main__":
    main()
