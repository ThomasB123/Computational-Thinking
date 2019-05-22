import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0
    '''
    'label' attribute is the distance from 
    the starting node to that node.
    Starting node is set to 0, all others
    initially set to -1 but will update.
    Output is 'label' value of target node
    once we reach it.
    '''

    # Colour code:
    # White - Undiscovered
    # Grey - Discovered but unprocessed (not fully explored)
    # Black - Has been processed (fully explored)
    for x in G.nodes:
        G.node[x]['color'] = "WHITE"
        #G.node[x]['label'] = 1000
    pi = [None]*len(G.nodes)
    G.node[a]['color'] = 'GREY'
    #G.node[a]['label'] = 0
    Q = []
    Q.append(a)
    while Q != []:
        u = Q.pop()
        adj = []
        for x in G.neighbors(u):
            adj.append(x)
        for v in adj:
            if G.node[v]['color'] == 'WHITE':
                G.node[v]['color'] = 'GREY'
                G.node[v]['label'] = G.node[u]['label'] + 1
                pi[v-1] = u
                Q.append(v)
            if v == b:
                return G.node[v]['label']
        G.node[u]['color'] = 'BLACK'



G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()


G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()


G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()


G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
