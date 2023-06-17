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


def encrypt(p, k, Zn):
    p = p.lower()
    p = p.replace(" ", "")
    o = ""
    for i in p:
        x = d[i]
        y = x + k
        k = x
        y %= Zn
        o += di[y]
    o = o.upper()
    return o

def decrypt(c, k, Zn):
    c = c.lower()
    o = ""
    for i in c:
        x = d[i]
        y = x - k
        k = y
        y %= Zn
        o += di[y]
    return o

if __name__ == "__main__":
    p = "rendezvous"
    c = encrypt(p, 8, 26)
    print(c)
    print(decrypt(c, 8, 26))

    c = "MALVVMAFBHBUQPTSOXALTGVWWRG"
    for i in range(0, 26):
        print(decrypt(c, i, 26))
