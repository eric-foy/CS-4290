import matrix_minors as mm
import matrix_determinant as md
import matrix_smprint as mp
import matrix_multiply as mmul
import matrix_identity as mi

def adjoint(A, Zn):
    x = []
    for i in range(0, len(A)):
        y = []
        for j in range(0, len(A[i])):
            d = md.determinant(mm.minors(A, j+1, i+1), Zn)
            z = (-1)**(i+j) * d
            z %= Zn
            y += [z]
        x += [y]
    check1(A, x, Zn)
    return x

def check1(A, Aa, Zn):
    B = mmul.mul(Aa, A, Zn)
    C = mmul.mul(A, Aa, Zn)
    d = md.det(A, Zn)
    I = mi.identity(len(A))
    D = []
    for i in I:
        x = []
        for j in i:
            y = d * j
            y %= Zn
            x += [y]
        D += [x]
    #mp.out(B)
    #mp.out(C)
    #mp.out(D)
    if B != C or B != D:
        print("Error in adjoint check1")

if __name__ == "__main__":
    A = [[3, 3, 6], [8, 4, 10], [1, 4, 6]]
    Aa = adjoint(A, 11)
    mp.out(Aa)
