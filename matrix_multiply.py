import sys
import matrix_smprint

def multiply(m, n):
    # no jagged matrices
    a = len(m[0])
    for i in m:
        if (len(i) != a):
            print("jagged matrix m")
            return None
    a = len(n[0])
    for i in n:
        if (len(i) != a):
            print("jagged matrix n")
            return None

    # num of col in m == num row in n
    if (len(m[0]) != len(n)):
        print("num of col in m != num row in n")
        return None

    # resulting matrix has: len(m) rows, len(n[0]) cols
    x = []
    for i in range(0, len(m)):
        y = []
        for j in range(0, len(n[0])):
            mx = 0
            for mi in range(0, len(n)):
                mx += m[i][mi]*n[mi][j]
            y += [mx]
        x += [y]
    return x

if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    m = multiply(a, b)
    #m = multiply(int(sys.argv[1]), int(sys.argv[2])
    print(matrix_smprint.smprint(m))
