import basex
import divmul
import invert

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

def encrypt(p, q, b, msg, blk):
    n = p*q
    encrypt(n, b, msg, blk)

def encrypt(n, b, msg, blk_s):
    o = ""
    for i in range(0, len(msg), blk_s):
        blk_a = []
        blk = msg[i:i+blk_s]
        for j in blk:
            blk_a += [d[j]]

        blk_a.reverse()
        x = basex.encode(blk_a, 26)
        x = divmul.divmul(x, b, n)

        y = basex.decode(x, 26)
        if len(y) < blk_s+1:
            y += [0]
        y.reverse()
        for j in y:
            o += di[j]
    o = o.upper()
    return o


def decrypt(p, q, a, msg, blk_s):
    n = p*q
    decrypt(n, a, msg, blk_s)

def decrypt(n, a, msg, blk_s):
    o = ""
    msg = msg.lower()
    blk_s = blk_s+1
    for i in range(0, len(msg), blk_s):
        blk_a = []
        blk = msg[i:i+blk_s]
        for j in blk:
            blk_a += [d[j]]

        blk_a.reverse()
        x = basex.encode(blk_a, 26)
        x = divmul.divmul(x, a, n)

        y = basex.decode(x, 26)
        if len(y) == blk_s-2:
            y += [0]
        elif len(y) != blk_s-1:
            print("block size mismatch")
        y.reverse()
        for j in y:
            o += di[j]
    o = o.lower()
    return o

def ikey(p, q, a):
    phi = (p - 1)*(q - 1)
    ai = invert.invert(a, phi)
    return ai

if __name__ == "__main__":
    n = 899
    b = 29
    blk_s = 2
    msg = "live"
    c = encrypt(n, b, msg, blk_s)
    print(c)
    a = ikey(29, 31, b)
    print(decrypt(n, a, c, blk_s))

    msg = "well"
    c = encrypt(n, b, msg, blk_s)
    print(c)
    a = ikey(29, 31, b)
    print(decrypt(n, a, c, blk_s))

    c = "ADOANE"
    a = ikey(29, 31, b)
    print(decrypt(n, a, c, blk_s))
