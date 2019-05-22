import networkx as nx

def Graph():
    G = nx.Graph()
    
    k = 6
    
    for i in range(1,2*k+1):
        G.add_node(i)
    
    for i in range(1,k+1):
        for j in range(1,k+1):
            if i!=j:
                G.add_edge(2*i-1,2*j)
    
    G.add_nodes_from(G.nodes(), color='never coloured')
    return G
