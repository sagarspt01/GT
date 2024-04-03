import networkx as nx
import datetime

current_time = datetime.datetime.now().time()
# print("Current time:", current_time)

specific_time1 = datetime.time(9, 0, 0)
# print("Specific time:", specific_time1)

specific_time2 = datetime.time(12, 0, 0)
# print("Specific time:", specific_time2)

specific_time3 = datetime.time(1, 0, 0)
# print("Specific time:", specific_time3)

specific_time4 = datetime.time(6, 0, 0)
# print("Specific time:", specific_time4)

specific_time5 = datetime.time(10, 0, 0)
# print("Specific time:", specific_time5)

# Function to find the minimum spanning tree of a graph
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

# Main function
def main():
    # Create the bigger graph with weights
    bigger_graph = nx.Graph()
    
    if(current_time > specific_time1 and current_time < specific_time2):
        bigger_graph.add_weighted_edges_from([
        ('A', 'B', 2),
        ('A', 'C', 3),
        ('B', 'C', 4),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('C', 'E', 6),
        ('D', 'E', 7)
    ])
    elif(current_time > specific_time2 and current_time < specific_time3):
        print("Break time")
        return
    elif(current_time > specific_time3 and current_time < specific_time4):
        bigger_graph.add_weighted_edges_from([
        ('P', 'Q', 2),
        ('P', 'R', 3),
        ('Q', 'R', 4),
        ('Q', 'S', 5),
        ('R', 'S', 1),
        ('R', 'T', 6),
        ('S', 'T', 7)
    ])
    elif(current_time > specific_time4 and current_time < specific_time5):
        bigger_graph.add_weighted_edges_from([
        ('P', 'Q', 2),
        ('P', 'R', 3),
        ('Q', 'R', 4),
        ('Q', 'S', 5),
        ('R', 'S', 1),
        ('R', 'T', 6),
        ('S', 'T', 7)
    ])
    else:
        print("Function Over")
        return
    print("Input the subgraph (list of nodes):")
    subgraph_nodes = input().split()

    # Extract subgraph from the bigger graph
    subgraph = bigger_graph.subgraph(subgraph_nodes)
    
    print("\nMinimum Spanning Tree Path of the subgraph:")
    mst = minimum_spanning_tree(subgraph)
    print("Path:", list(nx.dfs_edges(mst)))

if __name__ == "__main__":
    main()
