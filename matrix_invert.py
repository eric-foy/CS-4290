import matrix_determinant as md
import matrix_adjoint as ma
import invert as iZn
import matrix_invertable as mi
import matrix_smprint as mp

def invert(A, Zn):
    if not mi.invertableb(A, Zn):
        return None

    d = md.det(A, Zn)
    di = iZn.invert(d, Zn)
    B = ma.adjoint(A, Zn)
    x = []
    for i in B:
        y = []
        for j in i:
            z = di * j
            z %= Zn
            y += [z]
        x += [y]
    
    if not mi.invertable(A, x, Zn):
        print("Inverted X input != identity")
        return None

    return x

if __name__ == "__main__":
    A = [[1, 14], [14, 10]]
    Ai = invert(A, 29)
    print(mp.smprint(Ai))
