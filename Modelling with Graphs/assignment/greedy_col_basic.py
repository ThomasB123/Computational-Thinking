import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_smallest_color(G,i):
    n = len(G.nodes())
    colour = 1
    while True:
        check = True
        for x in G.edges(i):
            if G.node[x[1]]['color'] == colour:
                check = False
        if check:
            return colour
        colour += 1

def greedy(G):
    global kmax
    kmax = 0
    for x in range(1,len(G.nodes)+1):
        colour = find_smallest_color(G,x)
        G.node[x]['color'] = colour
        kmax = max(kmax,colour)
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)

print('Graph G1:')
G=graph1.Graph()
greedy(G)

print('Graph G2:')
G=graph2.Graph()
greedy(G)

print('Graph G3:')
G=graph3.Graph()
greedy(G)

print('Graph G4:')
G=graph4.Graph()
greedy(G)

print('Graph G5:')
G=graph5.Graph()
greedy(G)