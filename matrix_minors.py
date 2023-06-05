import matrix_smprint as mp

def minors(m, ith, jth):
    ith -= 1
    jth -= 1
    x = []
    for i in range(len(m)):
        if (i != ith):
            y = []
            for j in range(len(m[i])):
                if (j != jth):
                    y += [m[i][j]]
            x += [y]
    return x

if __name__ == "__main__":
    A = [[2, 1, 1], [5, 3, 2], [3, 3, 1]]
    print(mp.smprint(minors(A, 1, 1)))
    print(mp.smprint(minors(A, 1, 3)))
    print(mp.smprint(minors(A, 3, 2)))
