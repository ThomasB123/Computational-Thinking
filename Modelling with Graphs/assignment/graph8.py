import networkx as nx

def Graph():
    G = nx.Graph()

    k = 50
    
    for i in range(1,k+1):
        G.add_node(i)

    for i in range(1,k+1):
        for j in range(1,k+1):
            G.add_edge(i,j)


    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label = -1)
    G.add_nodes_from(G.nodes(), visited = 'no')

    return G
