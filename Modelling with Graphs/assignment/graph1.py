import networkx as nx

def Graph():
    G = nx.Graph()
    
    k = 6
    
    for i in range(1,2*k+2):
        G.add_node(i)
    
    G.add_edge(2,3)
    G.add_edge(3,4)    
    
    A = [1]
    B = [3]
    
    for i in range(2,k+1):
        A = A + [2*i+1]
        B = B + [2*i]
    
    for i in A:
        for j in B:
            if i!=j+1:
                if i!=1:
                    G.add_edge(i,j)
                else:
                    if j!=3:
                        G.add_edge(i,j)
    
    
    G.add_nodes_from(G.nodes(), color='never coloured')
    return G
