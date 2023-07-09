import sys

def encode(x, b):
    o = 0
    p = 0
    for i in x:
        o += i * b**p
        p += 1
    return o

def decode(x, b):
    o = []
    p = 0
    while x > b:
        o += [x % b]
        x = int(x / b)
    o += [x % b]
    return o

if __name__ == "__main__":
    x = int(sys.argv[1])
    b = int(sys.argv[2])
    d = decode(x, b)
    print(d)
    print(encode(d, b))
