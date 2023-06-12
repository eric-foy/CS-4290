import sys

def factor(n, f):
    for i in range(2, int(n/2)):
        if n % i == 0:
            f += [i]
            return factor(int(n / i), f)
    f += [n]
    return f

if __name__ == "__main__":
    print(factor(int(sys.argv[1]), []))
