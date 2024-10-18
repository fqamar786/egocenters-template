import networkx as nx

def find_impostor(edgelist, pseudocenters):
    # Step 1: Create the graph from the edgelist
    G = nx.Graph()
    G.add_edges_from(edgelist)
    
    # Step 2: Analyze ego networks of each vertex in pseudocenters
    ego_sizes = {}
    
    for vertex in pseudocenters:
        # Get the ego network centered on this vertex
        ego_net = nx.ego_graph(G, vertex)
        # Store the size of the ego network (number of nodes and edges)
        ego_sizes[vertex] = (len(ego_net.nodes()), len(ego_net.edges()))
    
    # Step 3: Identify the impostor
    # Since the impostor is not a true ego center, it is expected to have an ego network
    # that is smaller or structurally different from the others. Let's look for outliers.
    
    # To simplify, let's compare the ego network sizes and find the one that stands out
    avg_num_nodes = sum([size[0] for size in ego_sizes.values()]) / len(pseudocenters)
    impostor = None
    for vertex, size in ego_sizes.items():
        # If the ego network size is significantly smaller, we suspect it's the impostor
        if size[0] < avg_num_nodes * 0.8:  # 20% threshold difference
            impostor = vertex
            break
    
    return impostor
