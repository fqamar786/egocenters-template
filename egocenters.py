import networkx as nx

def find_impostor(edgelist, pseudocenters):
    # Step 1: Create the graph from edgelist
    G = nx.Graph()
    G.add_edges_from(edgelist)

    # Step 2: Find the ego network size for each vertex in pseudocenters
    ego_sizes = {}
    for center in pseudocenters:
        ego_network = nx.ego_graph(G, center)
        ego_sizes[center] = len(ego_network)
    
    # Step 3: Find the outlier based on ego network size
    # Sort the pseudocenters by their ego network size
    size_list = sorted(ego_sizes.values())
    
    # Step 4: Since there are 10 real ego centers, 1 outlier, look for an outlier size
    impostor = None
    for vertex, size in ego_sizes.items():
        if size != size_list[1]:  # If the size doesn't match the majority size
            impostor = vertex
            break
    
    return impostor

