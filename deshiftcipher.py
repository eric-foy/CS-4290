import sys

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

def deshiftcipher(e, key):
    e = e.upper()
    o = ""
    for i in e:
        a = d[i]
        a = a - key
        a = a % 26
        o += p[a]
        o = o.lower()
    print(o)

if __name__ == "__main__":
    deshiftcipher(sys.argv[1], int(sys.argv[2]))
