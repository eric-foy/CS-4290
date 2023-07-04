import invert

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

def mul(a, b, Zn):
    n = deg(a) + deg(b)

    c = []
    for i in range(0, n+1):
        #print("x^"+str(i))
        y = 0
        for j in range(0, i+1):
            for k in range(0, i+1):
                if j + k == i:
                    if j < len(a) and k < len(b):
                        #print(f"    a{j}*b{k} = {a[j]}*{b[k]}")
                        y += a[j] * b[k]
                        y %= Zn
        c += [y]
    return c

def omul(a, b, Zn):
    out(mul(a, b, Zn))

# polynomial long division
def div(a, b, Zn):
    # a / b
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
        for i in range(0, deg(c)+1):
            y = c[i] - d[i]
            y %= Zn
            e += [y]
        #out(e)
        c = e

    return [o, c]

def odiv(a, b, Zn):
    o = div(a, b, Zn)
    print("q = ")
    out(o[0])
    print("r = ")
    out(o[1])

def deg(a):
    d = len(a) - 1
    for i in a[::-1]:
        if i != 0:
            return d
        else:
            d -= 1

def coef(a):
    return a[deg(a)]

def test():
    a = [1, 2, 3, 0, 5]
    b = [1, 1]
    out(a)

    print(add([1, 1], [2, 2, 2], 100))
    oadd([1, 1], [2, 2, 2], 100)

    oadd([1, 1, 1], [0, 1, 1], 2)

    print(mul([1, 1, 1], [0, 1, 1], 100))
    omul([1, 1, 1], [0, 1, 1], 100)

    omul([1, 1, 1], [0, 1, 1], 2)

    print()
    print(div([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 5))
    odiv([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 5)
    odiv([0, 0, 0, 0, 0, 1], [1, 1, 0, 1], 2)
    odiv([1, 0, 1, 1, 3, 6], [6, 5, 3], 7)
    odiv([1, 1, 0, 0, 1, 1], [1, 0, 0, 1], 2)
    

    #div([0, 0, 0, 0, 0, 3], [2, 2, 0, 2], 5)

if __name__ == "__main__":
    test()
