import sympy

def encrypt(p, c, n):
    z = ""
    for i in range(0, len(c)):
        if p[i] == "0" and c[i] == "0":
            z += "0"
        elif p[i] == "0" and c[i] == "1":
            z += "1"
        elif p[i] == "1" and c[i] == "0":
            z += "1"
        elif p[i] == "1" and c[i] == "1":
            z += "0"
    # now solve a system of n linear equations.
    A = []
    for i in range(0, n):
        V = []
        for j in range (0, n):
            V += [int(z[i+j])]
        V += [-int(z[i+n])]
        A += [V]
    B = sympy.Matrix(A)
    C = B.rref()[0]
    D = C.tolist()
    co = ""
    for i in range(0, n):
        co += str(D[i][-1] % 2)

    for i in range(len(c), len(p)):
        zm = 0
        for j in range(0, n):
            m = i - n + j
            if c[j] == "0" and z[m] == "0":
                zm += 0
            elif c[j] == "0" and z[m] == "1":
                zm += 0
            elif c[j] == "1" and z[m] == "0":
                zm += 0
            elif c[j] == "1" and z[m] == "1":
                zm += 1
        zm %= 2
        z += str(zm)

    q = ""
    for i in range(0, len(p)):
        if p[i] == "0" and z[i] == "0":
            q += "0"
        elif p[i] == "0" and z[i] == "1":
            q += "1"
        elif p[i] == "1" and z[i] == "0":
            q += "1"
        elif p[i] == "1" and z[i] == "1":
            q += "0"
    print(q)



if __name__ == "__main__":
    p = "010001100000000"
    c = "0110111001"
    encrypt(p, c, 5)
