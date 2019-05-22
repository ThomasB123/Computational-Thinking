#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G

#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v
#print(decimalToVector(9,4))

# Functions for Hamming codes:

def message(a):
    # output has length k=2**r-r-1
    # for some r >= 2 where k-r > len(a)
    # lowest r where this is true is used
    # output:
    # Length of a in binary
    # a
    # 0s to fill any remaining space
    length = len(a)
    r = 2
    k = 1
    while k-r < length:
        r += 1
        k = 2**r-r-1
    out = decimalToVector(length,r)
    out.extend(a)
    leftover = k-len(out)
    for x in range(leftover):
        out.append(0)
    return out
'''
a = [1]
a = [0,0,1]
a = [0,1,1,0]
a = [1,1,1,1,0,1]
a = [0,1,1,0,1]
print(message(a))
'''
def hammingEncoder(m):
    # m * Generator Matrix
    length = len(m)
    r = 2
    k = 1
    while k < length:
        r += 1
        k = 2**r-r-1
    if length != k:
        return []
    G = hammingGeneratorMatrix(r)
    out = []
    for x in range(len(G[0])):
        add = 0
        for y in range(length):
            add += m[y]*G[y][x]
        out.append(add%2)
    return out
'''
m = [1,1,1]
m = [1,0,0,0]
m = [0]
m = [0,0,0]
m = [0,0,1,1]
print(hammingEncoder(m))
'''
def hammingDecoder(v):
    # return hamming Encoder output
    # that is closest to v
    # will be either the same
    # or be off by one
    # (hamming distance of 0 or 1)
    length = len(v)
    r = 2
    k = 3
    while k < length:
        r += 1
        k = 2**r-1
    if length != k:
        return []
    k -= r
    encoded = []
    for x in range(2**k):
        encoded.append(hammingEncoder(decimalToVector(x,k)))
    for x in encoded:
        count = 0
        for i in range(length):
            if v[i] != x[i]:
                count += 1
        if count == 0 or count == 1:
            return x
    return []
'''
v = [0,1,1,0,0,0,0]
v = [1,0,1,1]
v = [1,1,0]
v = [1,0,0,0,0,0,0]
print(hammingDecoder(v))
'''
def messageFromCodeword(c):
    # Reverses hamming Encoder
    length = len(c)
    r = 2
    k = 3
    while k < length:
        r += 1
        k = 2**r-1
    if length != k:
        return []
    k = 2**r-r-1
    for x in range(2**k):
        binary = decimalToVector(x,k)
        encoded = hammingEncoder(binary)
        if c == encoded:
            return binary
    return []
'''
c = [1,1,0,1]
c = [1,1,1,0,0,0,0]
c = [1,1,1,1,1,1,1]
c = [0,0,0,0]
print(messageFromCodeword(c))
'''
def dataFromMessage(m):
    # Reverses message
    length = len(m)
    r = 2
    k = 1
    while k < length:
        r += 1
        k = 2**r-r-1
    if length != k:
        return []
    tot = 0
    mul = 1
    for x in range(r-1,-1,-1):
        tot += m[x]*mul
        mul *= 2
    if length < r+tot:
        return []
    for x in range(r+tot,length):
        if m[x] != 0:
            return []
    out = m[r:r+tot]
    return out
'''
m = [1,0,0,1,0,1,1,0,1,0]
m = [1,1,1,1,0,1,1,0,1,0,0]
m = [0,1,0,1,0,0,1,0,1,0,0]
m = [0,1,1,0,0,1,1,1,1,1]
m = [0,0,1,1]
m = [1,1,1,1]
print(dataFromMessage(m))
'''
# Functions for repition codes:

def repetitionEncoder(m,n):
    # repeat m, n times
    out = []
    if len(m) == 1 and n > 0 and (m[0] == 0 or m[0] == 1):
        for x in range(n):
            out.extend(m)
    return out
'''
m = [1]
n = 4
print(repetitionEncoder(m,n))
'''
def repetitionDecoder(v):
    # finds which number has been repeated
    length = len(v)
    if length <= 0:
        return []
    count0 = 0
    count1 = 0
    x = 0
    if v[0] == 0:
        count0 += 1
        x += 1
        while x < length and v[x] == 0:
            count0 += 1
            x += 1
        while x < length and v[x] == 1:
            count1 += 1
            x += 1
        if length > x:
            return []
    if v[0] == 1:
        count1 += 1
        x += 1
        while x < length and v[x] == 1:
            count1 += 1
            x += 1
        while x < length and v[x] == 0:
            count0 += 1
            x += 1
        if length > x:
            return []
    if count0 == count1:
        return []
    if count0 > count1:
        return [0]
    if count1 > count0:
        return [1]
    return []
'''
v = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
v = [1,2]
v = [1,1,0,0]
v = [1,0,0,0]
v = [0,0,1]
v = [1,1,1,1]
print(repetitionDecoder(v))
'''