import sys

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

p = {}
for i in d:
    p[d[i]] = i

def shiftcipher(msg, key):
    msg = msg.replace(' ', '')
    msg = msg.lower()
    o = ""
    for i in msg:
        a = d[i]
        a = a + key
        a = a % 26
        o += p[a]
        o = o.upper()
    print(o)

if __name__ == "__main__":
    shiftcipher(sys.argv[1], int(sys.argv[2]))
