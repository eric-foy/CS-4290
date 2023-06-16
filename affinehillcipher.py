import matrix_invert as mi
import matrix_multiply as mm
import matrix_smprint as mp

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

def encrypt(msg, keya, keyb, Zn):
    msg = msg.replace(' ', '')
    msg = msg.lower()
    o = ""
    m = len(keya)
    for i in range(0, len(msg), m):
        x = []
        for j in msg[i:i+m]:
            x += [d[j]]
        y = mm.mul([x], keya, Zn)
        for j in range(0, len(y[0])):
            z = y[0][j] + keyb[j]
            z %= Zn
            o += di[z]
        o = o.upper()
    return o


def decrypt(msg, keya, keyb, Zn):
    msg = msg.lower()
    o = ""
    m = len(keya)
    for i in range(0, len(msg), m):
        x = []
        for j in msg[i:i+m]:
            x += [d[j]]
        for j in range(0, len(keyb)):
            x[j] = x[j] - keyb[j]
            x[j] = x[j] % Zn
        keyai = mi.invert(keya, Zn)
        y = mm.mul([x], keyai, Zn)
        for j in y[0]:
            o += di[j]
    return o

if __name__ == "__main__":
    p = "a displayed equation"
    keya2 = [[3, 6, 4], [5, 15, 18], [17, 8, 5]]
    keyb2 = [8, 13, 1]
    c = encrypt(p, keya2, keyb2, 26)

    print(decrypt(c, keya2, keyb2, 26))
