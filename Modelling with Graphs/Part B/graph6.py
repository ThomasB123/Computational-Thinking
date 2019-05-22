import networkx as nx

def Graph():
    G = nx.Graph()

    k = 50
    
    for i in range(1,k+2):
        G.add_node(i)

    for i in range(2,k+2):
        G.add_edge(1,i)


    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label = -1)
    G.add_nodes_from(G.nodes(), visited = 'no')

    return G
