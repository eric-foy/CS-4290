import matrix_multiply as mm
import matrix_invert as mi

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

# k is a dict
def decrypt(k, n, msg, Zn):
    km = []
    for i in range(1, n+1):
        y = []
        for j in range(1, n+1):
            if i == k[j]:
                y += [1]
            else:
                y += [0]
        km += [y]

    km = mi.invert(km, Zn)

    msg = msg.lower()
    msg = msg.replace(" ", "")
    msgm = []
    for i in msg:
        msgm += [d[i]]
    o = ""
    for i in range(0, len(msgm), n):
        x = mm.mul([msgm[i:i+n]], km, Zn)
        for j in x[0]:
            o += di[j]
    o = o.lower()
    return o

def encrypt(k, n, msg, Zn):
    km = []
    for i in range(1, n+1):
        y = []
        for j in range(1, n+1):
            if i == k[j]:
                y += [1]
            else:
                y += [0]
        km += [y]

    msg = msg.lower()
    msg = msg.replace(" ", "")
    msgm = []
    for i in msg:
        msgm += [d[i]]
    o = ""
    for i in range(0, len(msgm), n):
        x = mm.mul([msgm[i:i+n]], km, Zn)
        for j in x[0]:
            o += di[j]
    o = o.upper()
    return o

if __name__ == "__main__":
    k = {1:3, 2:5, 3:1, 4:6, 5:4, 6:2}
    p = "she sells sea shells by the sea shore"
    c = encrypt(k, len(k), p, 26)
    print(c)

    print(decrypt(k, len(k), c, 26))

    
