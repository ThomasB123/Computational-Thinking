import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10

def max_distance(G):
    diameter = 0
    for a in G.nodes:
        G.add_nodes_from(G.nodes(), label = -1)
        G.node[a]['label'] = 0
        Q = []
        Q.append(a)
        while Q != []:
            u = Q.pop()
            adj = []
            for x in G.neighbors(u):
                adj.append(x)
            for v in adj:
                if G.node[v]['label'] == -1:
                    G.node[v]['label'] = G.node[u]['label'] + 1
                    Q.append(v)
                    diameter = max(diameter,G.node[v]['label'])
    return diameter

print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()

G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()

G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()

G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()

G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()