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

def decrypt(c, p, k):
    c = c.lower()

    pi = {}
    for i in p:
        pi[p[i]] = i

    o = ""
    for i in range(0, len(c)):
        z = k + i
        y = d[c[i]]
        y -= z
        y %= 26
        o += di[pi[y]]

    return o


if __name__ == "__main__":
    p = {0:23,
          1:13,
          2:24,
          3:0,
          4:7,
          5:15,
          6:14,
          7:6,
          8:25,
          9:16,
          10:22,
          11:1,
          12:19,
          13:18,
          14:5,
          15:11,
          16:17,
          17:2,
          18:21,
          19:12,
          20:20,
          21:4,
          22:10,
          23:9,
          24:3,
          25:8}
    # k in Z26
    c = "WRTCNRLDSAFARWKXFTXCZRNHNYPDTZUUKMPLUSOXNEUDOKLXRMCBKGRCCURR"
    for i in range(0, 26):
        print(decrypt(c, p, i))
