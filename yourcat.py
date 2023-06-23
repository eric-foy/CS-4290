import sys

def deexamcipher(msg):
    n = int(len(msg)/2)
    a = msg[:n+1]
    b = msg[n+1:]
    print(a)
    print(b)
    o = ""
    for i in range(0, n):
        o += a[i]
        o += b[i]
    o += a[-1]
    print(o.lower())

if __name__ == "__main__":
    deexamcipher(sys.argv[1])
