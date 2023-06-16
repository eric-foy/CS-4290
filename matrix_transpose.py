def transpose(A):
    At = []
    for i in range(0, len(A[0])):
        y = []
        for j in range(0, len(A)):
            y += [A[j][i]]
        At += [y]
    return At


def T(A):
    return transpose(A)

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    print(T(A))
