import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_next_vertex(G):
    next = 1
    for x in G.nodes():
        if next != 1:
            return next
        if G.node[x]['visited'] == 'no':
            for y in G.edges(x):
                if G.node[y[1]]['visited'] == 'yes':
                    next = x
    return next

def find_smallest_color(G,i):
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
    for x in G.nodes:
        a = find_next_vertex(G)
        colour = find_smallest_color(G,a)
        G.node[a]['color'] = colour
        G.node[a]['visited'] = 'yes'
        kmax = max(kmax,colour)
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()

print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)