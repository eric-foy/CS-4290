import divmul
import invert
import polys
import basex

d = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
}

di = {}
for i in d:
    di[d[i]] = i

def encrypt(alpha, beta, k, Zn, msg):
    y1 = divmul.power(alpha, k, Zn)
    y2 = msg * divmul.power(beta, k, Zn)
    y2 %= Zn
    return (y1, y2)

def decrypt(a, Zn, y):
    x = divmul.power(y[0], a, Zn)
    x = invert.invert(x, Zn)
    o = y[1] * x
    o %= Zn
    return o

# len(msg) = 1
def poly_encrypt(alpha, beta, k, F, f, msg):
    msg = msg.upper()

    if not polys.primitive(alpha, F, f):
        print(f"{sout(alpha)} not primitive")
        return ("-1", "-1")

    y1 = polys.power(alpha, k, F, f)

    a = basex.decode(d[msg], F)
    b = polys.power(beta, k, F, f)
    y2 = polys.mul(a, b, F)
    y2 = polys.div(y2, f, F)[1]
    
    polys.out(y1)
    polys.out(y2)

    y1enc = basex.encode(y1, F)
    y2enc = basex.encode(y2, F)

    return (di[y1enc], di[y2enc])

def decrypt(a, Zn, y):
    x = divmul.power(y[0], a, Zn)
    x = invert.invert(x, Zn)
    o = y[1] * x
    o %= Zn
    return o

def poly_decrypt(a, F, f, y):
    y1enc = d[y[0]]
    y2enc = d[y[1]]

    y1dec = basex.decode(y1enc, F)
    y2dec = basex.decode(y2enc, F)
    
    x = polys.power(y1dec, a, F, f)
    x = polys.inv(x, F, f)
    o = polys.mul(y2dec, x, F)
    o = polys.div(o, f, F)[1]

    oenc = basex.encode(o, F)
    ostr = di[oenc]
    ostr = ostr.lower()
    return ostr

if __name__ == "__main__":
    c = encrypt(2, 949, 853, 2579, 1229)
    print(c)
    print(decrypt(765, 2579, c))

    print()
    x = basex.decode(d["J"], 3)
    polys.out(x)
    x = basex.decode(d["Z"], 3)
    polys.out(x)
    x = basex.decode(d["N"], 3)
    polys.out(x)
    x = basex.decode(d["S"], 3)
    polys.out(x)


    print()
    F = 3
    f = [1, 0, 2, 1]
    a = 9
    alpha = [2, 1]
    beta = polys.power(alpha, a, F, f)
    polys.out(f)
    polys.out(alpha)
    polys.out(beta)

    print()
    y = poly_encrypt(alpha, beta, 1, F, f, "u")
    print(y)
    print(poly_decrypt(a, F, f, y))
    y = poly_encrypt(alpha, beta, 2, F, f, "s")
    print(y)
    print(poly_decrypt(a, F, f, y))
    y = poly_encrypt(alpha, beta, 3, F, f, "a")
    print(y)
    print(poly_decrypt(a, F, f, y))
