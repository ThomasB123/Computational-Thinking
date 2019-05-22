import networkx as nx

def Graph():
    G = nx.Graph()
    
    k = 5
    
    for i in range(1,2*k+4):
        G.add_node(i)
    
    G.add_edge(1,2)
    G.add_edge(1,k+2)
    
    for i in range(2,k+2):
        for j in range(k+2,2*k+2):
            if j-i!=k:
                G.add_edge(i,j)
    
    x = 2*k + 2
    y = 2*k + 3
    G.add_edges_from([(x,1),(x,2),(y,1),(y,2),(x,y)])
    
    G.add_nodes_from(G.nodes(), color='never coloured')
    return G
