import networkx as nx

def Graph():
    G = nx.Graph()
    
    k=10
    
    for i in range(1,2*k+1):
        G.add_node(i)
    
    S=[(1, 2), (1, 5), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9), (4, 5), (5, 10), (6, 9), (6, 8), (7, 9), (7, 10), (8, 10)]
    #print(S)
    G.add_edges_from(S)

    for (i,j) in S:
        G.add_edge(k+i,k+j)

    for i in range(1,k+1):
        for j in range(k+1,2*k+1):
            G.add_edge(i,j)


    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label = -1)
    G.add_nodes_from(G.nodes(), visited = 'no')

    return G
