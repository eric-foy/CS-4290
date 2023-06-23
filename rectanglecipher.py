import matrix_transpose as mt
import matrix_smprint as mp
import divisors

def encrypt(p, m, n):
    pm = []
    for i in range(0, m):
        y = []
        for j in range(0, n):
            y += [p[i*n + j]]
        pm += [y]

    pm = mt.T(pm)

    o = ""
    for i in pm:
        for j in i:
            o += j
    o = o.upper()
    return o

def decrypt(c, m, n):
    if m*n > len(c):
        c += "_" * (m*n - len(c))
    pm = []
    for i in range(0, n):
        y = []
        for j in range(0, m):
            y += [c[i*m + j]]
        pm += [y]
    
    #mp.out(pm)
    pm = mt.T(pm)

    o = ""
    for i in pm:
        for j in i:
            o += j
    o = o.lower()
    o = o.replace("_", "")
    return o

def evenblocks(c):
    cn = divisors.of(len(c))
    cni = []
    for i in cn:
        cni += [int(len(c) / i)]

    for i in range(0, len(cn)):
        print()
        print(cn[i], "by", cni[i])
        print(decrypt(c, cn[i], cni[i]))

if __name__ == "__main__":
    p = "cryptography"
    m = 3
    n = 4
    c = encrypt(p, m, n)
    print(c)

    print(decrypt(c, m, n))

    c = "MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW"
    cblock = int(len(c)/7)
    o = ""
    for i in range(0, len(c), cblock):
        o += decrypt(c[i:i+cblock], 2, 3)

    print(o)


def bla(c):
    for i in range(1, 42):
        for j in range(1, 42):
            if i*j < 80:
                print(decrypt(c, i, j))
