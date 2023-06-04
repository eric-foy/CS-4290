def smprint(m):
    o = ""
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            o += str(m[i][j]) + ' '
        o += '\n'
    return o
