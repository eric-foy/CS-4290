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

def deg(a):
    return len(a) - 1

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

if __name__ == "__main__":
    test()
