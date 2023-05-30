import sys
import invert

def findSolutions(n):
    a = []
    m = []
    M = []
    mm = 1
    Mi = []
    x = 0
    for i in range(2, n*2 + 2, 2):
        a += [int(sys.argv[i])]
    for i in range(3, n*2 + 3, 2):
        m += [int(sys.argv[i])]
    for i in m:
        mm*=i
    for i in m:
        M += [int(mm / i)]
    for i in range(0, n):
        Mi += [invert.invert(M[i], m[i])]
    for i in range(0, n):
        x += a[i]*M[i]*Mi[i]
    x = x % mm
    return x

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(findSolutions(n))
