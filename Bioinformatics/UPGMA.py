import time
import networkx as nx
import matplotlib.pyplot as plt

def UPGMA(a):
    start = time.time()
    text = open(a,'r')
    inp = text.read()
    text.close()
    print()
    print(inp)
    print()
    lines = inp.split('\n')
    matrix = []
    for x in lines:
        matrix.append(x.split(' '))
    G = nx.Graph()
    for i in range(1,len(matrix[0])):
        G.add_node(matrix[0][i])
    while len(matrix) > 2:
        x = 1
        y = 2
        smallest = matrix[x][y]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] != '0' and float(matrix[i][j]) < float(smallest):
                    smallest = matrix[i][j]
                    x = i
                    y = j
        nodea = matrix[0][x]
        nodeb = matrix[0][y]
        new = nodea+nodeb
        G.add_node(new)
        G.add_edge(nodea,new)
        G.add_edge(new,nodeb)
        matrix[0].append(new)
        matrix.append([new])
        for i in range(1,len(matrix)-1):
            data = len(nodea) * float(matrix[i][x]) + len(nodeb) * float(matrix[i][y])
            matrix[-1].append(str(data/len(new)))
            matrix[i].append(str(data/len(new)))
        matrix[-1].append('0')
        matrix.pop(x)
        matrix.pop(y-1)
        for i in matrix:
            i.pop(x)
            i.pop(y-1)
        out = ''
        for i in matrix:
            for j in i:
                out += j + ' '
            out += '\n'
        print(out)
    nx.draw(G)
    plt.savefig(a+".png",format="PNG")
    end = time.time()
    print('Execution Time:',end-start)

UPGMA("matrix4.txt")