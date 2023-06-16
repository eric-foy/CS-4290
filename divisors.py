def of(a):
    o = []
    for i in range(1, a):
        if a % i == 0:
            o += [i]
    return o
