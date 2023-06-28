def add(A, B, Zn):
    if (len(A) != len(B)):
        print("row mismatch")

    # assume not jagged
    if (len(A[0]) != len(B[0])):
        print("column mismatch")

    C = []
    for i in range(0, len(A)):
        x = []
        for j in range(0, len(A[0])):
            y = A[i][j] + B[i][j]
            y %= Zn
            x += [y]
        C += [x]

    return C

if __name__ == "__main__":
    A = [[2, 2, 2], [2, 2, 2]]
    B = [[3, 3, 3], [3, 3, 3]]
    print(add(A, B, 100))
    print(add(A, B, 3))
