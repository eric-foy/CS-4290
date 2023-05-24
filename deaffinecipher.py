import sys
import invert

d = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
}

p = {}
for i in d:
    p[d[i]] = i

def deaffinecipher(msg, keya, keyb):
    msg = msg.upper()
    o = ""
    for i in msg:
        x = d[i]
        x = invert.invert(keya, 26)*(x - keyb)
        x = x % 26
        o += p[x]
        o = o.lower()
    print(o)

if __name__ == "__main__":
    deaffinecipher(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
