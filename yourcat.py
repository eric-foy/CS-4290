import sys

def encrypt(p):
    y1 = ""
    for i in range(0, len(p), 2):
        y1 += p[i]
    y2 = ""
    for i in range(1, len(p), 2):
        y2 += p[i]
    y = y1 + y2
    return y

def decrypt(msg):
    n = int(len(msg)/2)
    if (len(msg) % 2 == 0):
        a = msg[:n]
        b = msg[n:]
    else:
        a = msg[:n+1]
        b = msg[n+1:]
    print(a)
    print(b)
    o = ""
    for i in range(0, n):
        o += a[i]
        o += b[i]
    if (len(msg) % 2 == 1):
        o += a[-1]
    return o.lower()
