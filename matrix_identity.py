import sys
import matrix_smprint

def identity(n):
    a = []
    for i in range(0, n):
        b = []
        for j in range(0, n):
            b += [0]
        a += [b]

    c = 0
    for i in range(0, n):
        for j in range(0, n):
            if (j == c):
                a[i][j] = 1
        c += 1
    return a


if __name__ == "__main__":
    m = identity(int(sys.argv[1]))
    print(matrix_smprint.smprint(m))
