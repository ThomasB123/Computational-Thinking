def hammingGeneratorMatrix(r):
    n = 2**r-1
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))
    G = []
    for i in range(n):
        G.append(GG[rho[i]])
    G = [list(i) for i in zip(*G)]
    return G

def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

def message(a):
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

def hammingEncoder(m):
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

def hammingDecoder(v):
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

def messageFromCodeword(c):
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

def dataFromMessage(m):
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

def repetitionEncoder(m,n):
    out = []
    if len(m) == 1 and n > 0 and (m[0] == 0 or m[0] == 1):
        for x in range(n):
            out.extend(m)
    return out

def repetitionDecoder(v):
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