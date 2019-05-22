import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5
###
import matplotlib.pyplot as plt 
###
def find_smallest_color(G,i):
    neighbours = G.edges(i)
    check = 1
    for x in neighbours:
        colour = False
        for y in neighbours:
            if G.node[y[1]]['color'] == check:
                colour = True
        if not colour:
            return check
        check += 1
    return check

def greedy(G):
    global kmax
    kmax = 0
    for x in range(1,len(G.nodes)+1):
        check = find_smallest_color(G,x)
        G.node[x]['color'] = check
        if check > kmax:
            kmax = check
    
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    
    nx.draw(G,with_labels=True)
    plt.show()

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
