import invert
import itertools

def out(p):
    o = ""
    for i in range(0, len(p)):
        if p[i] != 0:
            if p[i] != 1 or i == 0:
                o += str(p[i])

            if i == 1:
                o += "x"
            elif i > 1:
                o += "x^"+str(i)

            o += " + "
    o = o[:-3]
    print(o)

def sout(p):
    o = ""
    for i in range(0, len(p)):
        if p[i] != 0:
            if p[i] != 1 or i == 0:
                o += str(p[i])

            if i == 1:
                o += "x"
            elif i > 1:
                o += "x^"+str(i)

            o += " + "
    o = o[:-3]
    return o

def largest(a, b):
    if len(a) > len(b):
        return len(a)
    else:
        return len(b)

def add(a, b, Zn):
    n = largest(a, b)

    c = []
    for i in range(0, n):
        if i >= len(a):
            y = b[i]
        elif i >= len(b):
            y = a[i]
        else:
            y = a[i] + b[i]
        y %= Zn
        c += [y]

    return c

def oadd(a, b, Zn):
    out(add(a, b, Zn))

def sub(a, b, Zn):
    n = largest(a, b)

    c = []
    for i in range(0, n):
        if i >= len(a):
            y = -b[i]
        elif i >= len(b):
            y = a[i]
        else:
            y = a[i] - b[i]
        y %= Zn
        c += [y]

    return c

def osub(a, b, Zn):
    out(sub(a, b, Zn))
    
def mul(a, b, Zn, disp=False):
    n = deg(a) + deg(b)

    c = []
    for i in range(0, n+1):
        if disp:
            print("x^"+str(i))
        y = 0
        for j in range(0, i+1):
            for k in range(0, i+1):
                if j + k == i:
                    if j < len(a) and k < len(b):
                        if disp:
                            print(f"    a{j}*b{k} = {a[j]}*{b[k]}")
                        y += a[j] * b[k]
                        y %= Zn
        c += [y]
    return c

def omul(a, b, Zn, disp=False):
    out(mul(a, b, Zn, disp))

# polynomial long division
def div(a, b, Zn, disp=False):
    if (deg(b) == -1):
        print("error: divide by zero")
        return ([-1], [-1])
    elif (deg(a) == -1):
        return([0], [0])

    # a / b
    if disp:
        print("long division:")
        out(a)
        out(b)

    o = [0]*(deg(a)-deg(b)+1)
    c = a
    while deg(b) <= deg(c):
        d = []
        for i in b:
            d += [i]

        x = deg(c) - deg(b)
        for i in range(0, x):
            d.insert(0, 0)

        co = invert.div(coef(c), coef(b), Zn)
        o[x] = co
        if (co == -1):
            return [-1, -1]
        for i in range(0, len(d)):
            d[i] = d[i]*co
            d[i] = d[i] % Zn
        #out(d)
        e = []
        if deg(c) != deg(d):
            # leading term in c - leading term in d should = 0
            # so, same length lists
            print("long division size mismatch")
            return [-1, -1]
        for i in range(0, deg(c)+1):
            y = c[i] - d[i]
            y %= Zn
            e += [y]
        #out(e)
        c = e

    return [o, c]

def odiv(a, b, Zn, disp=False):
    o = div(a, b, Zn, disp)
    print("q = ")
    out(o[0])
    print("r = ")
    out(o[1])

# irreducible polynomial generator
def primes(n, Zn):
    o = []
    x = range(0, Zn)
    y = [list(p) for p in itertools.product(x, repeat=(n+1))]
    for i in y:
        if deg(i) == n and coef(i) == 1:
            prime = True
            for j in range(2, n+1):
                z = [list(p) for p in itertools.product(x, repeat=j)]
                for k in z:
                    # only non trivial
                    if deg(i) > 0 and deg(k) > 0 and i != k:
                        d = div(i, k, Zn)
                        # no remainer and non trivial quotent
                        if deg(d[1]) == -1 and deg(d[0]) > 0:
                            prime = False
            if prime:
                o += [i]

    return o

def oprimes(n, Zn):
    p = primes(n, Zn)
    print()
    print(f"primes degree {n} mod {Zn}")
    for i in p:
        out(i)

def factors(a, Zn):
    o = []
    x = range(0, Zn)
    for j in range(2, deg(a)+1):
        z = [list(p) for p in itertools.product(x, repeat=j)]
        for k in z:
            # only non trivial
            if deg(a) > 0 and deg(k) > 0 and a != k:
                d = div(a, k, Zn)
                # no remainer and non trivial quotent
                if deg(d[1]) == -1 and deg(d[0]) > 0:
                    o += [(k, d[0])]
    return o

def ofactors(a, Zn):
    f = factors(a, Zn)
    for i in f:
        print(f"({sout(i[0])}) * ({sout(i[1])})")

def evaluate(a, b, Zn, disp=False):
    s = a[0]
    for i in range(1, len(a)):
        s += a[i] * b**i
        s %= Zn
    if disp:
        print(f"f({b})={s}")
    return s

def roots(a, Zn):
    o = []
    for i in range(0, Zn):
        b = evaluate(a, i, Zn)
        if b == 0:
            o += [i]
    return o

# root can be used multiple times
# i.e. in Z2 x^2 + 1 = (x-1)(x-1)
# we only print x^2 + 1 = (x-1)
def oroots(a, Zn):
    r = roots(a, Zn)
    o = sout(a)+" = "
    for i in r:
        o += f"(x-{i})"
    print(o)

# Zn / f(x)
# f(x) must be irreducable for field
# should be size p^deg(f)
def field(Zn, f):
    x = range(0, Zn)
    o = [list(p) for p in itertools.product(x, repeat=(deg(f)))]
    return o

def ofield(Zn, f):
    a = field(Zn, f)
    for i in a:
        out(i)

# -1 is negative infinity
def deg(a):
    d = len(a) - 1
    for i in a[::-1]:
        if i != 0:
            return d
        else:
            d -= 1
    return -1

def coef(a):
    return a[deg(a)]

def test():
    a = [1, 2, 3, 0, 5]
    b = [1, 1]
    out(a)

    print(add([1, 1], [2, 2, 2], 100))
    oadd([1, 1], [2, 2, 2], 100)

    oadd([1, 1, 1], [0, 1, 1], 2)

    print(mul([1, 1, 1], [0, 1, 1], 100, True))
    omul([1, 1, 1], [0, 1, 1], 100)

    omul([1, 1, 1], [0, 1, 1], 2)

    print()
    print(div([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 5))
    odiv([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 5, True)
    odiv([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 2, True)
    odiv([1, 0, 1, 1, 3, 6], [6, 5, 3], 7, True)
    odiv([1, 1, 0, 0, 1, 1], [1, 0, 0, 1], 2, True)
    odiv([1, 0, 2, 1, 1, 1], [1, 0, 1], 3, True)
    #div([0, 0, 0, 0, 0, 3], [2, 2, 0, 2], 5)

    print()
    oprimes(3, 3)
    o = []
    for i in primes(3, 3):
        o += [i[::-1]]
    o.sort()
    for i in o:
        print(i)

    print()
    o = []
    for i in primes(4, 3):
        o += [i[::-1]]
    o.sort()
    for i in o:
        print(i)

    print()
    print(factors([1, 0, 1], 5))
    ofactors([1, 0, 1], 5)

    print()
    print(roots([1, 0, 1], 5))
    oroots([1, 0, 1], 5)

    print()
    a = field(3, [1, 2, 0, 1])
    print(a)
    print(len(a))
    ofield(3, [1, 2, 0, 1])

    print()
    osub([1, 2, 0, 0, 0, 1], [0, 0, 2, 1], 5)
    osub([0, 0, 2, 1], [1, 2, 0, 0, 0, 1], 5)

if __name__ == "__main__":
    test()
