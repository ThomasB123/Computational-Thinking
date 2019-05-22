import networkx as nx

def Graph():
    G = nx.Graph()
    
    k = 6
    
    for i in range(1,2*k+2):
        G.add_node(i)
    
    for i in range(1,k+1):
        for j in range(1,k+1):
            if i!=j:
                G.add_edge(2*i,2*j+1)
    
    G.add_edge(1,2)
    
    for i in range(2,2*k+2):
            G.add_edge(1,i)
    
    
    G.add_nodes_from(G.nodes(), color='never coloured')
    return G
