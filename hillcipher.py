import matrix_multiply as mm

d = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
}

di = {}
for i in d:
    di[d[i]] = i

def hillcipher(k, n, p, Zn):
    o = ""
    for i in range(0, len(p), n):
        x = []
        for j in p[i:i+n]:
            x += [d[j]]
        y = mm.mul([x], k, Zn)
        for j in y[0]:
            o += di[j]
    o = o.upper()
    return o

if __name__ == "__main__":
    k = [[11, 8], [3, 7]]
    p = "july"
    n = 2
    Zn = 26
    c = hillcipher(k, n, p, Zn)
    print(c)
