from main_functions import *
from pprint import pprint

def main(A):
    # Define a matrix
    #A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

    # Factorize with Cholesky decomposition
    L = cholesky(A)

    # Lower-triangular into upper-triangular
    R = transpose(L)

    # Construct preliminary diagonal matrix for the method
    S = intermediate_diagonal_inverse_matrix(R)

    # Solve R*X = S to find X which is A^-1 (inverted matrix A)
    X = krishnamoorthy_menon_method(R, S)
    #print(X[0])

def main_with_prints():
    # Define a matrix
    A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

    print("A: ", end="")
    pprint(A)
    print()

    # Factorize with Cholesky decomposition
    L = cholesky(A)

    print("L: ", end="")
    pprint(L)
    print()

    # Lower-triangular into upper-triangular
    R = transpose(L)

    print("R: ", end="")
    pprint(R)
    print()

    # Construct preliminary diagonal matrix for the method
    S = intermediate_diagonal_inverse_matrix(R)

    print("S: ", end="")
    pprint(S)
    print()

    # Solve R*X = S to find X which is A^-1 (inverted matrix A)
    X = krishnamoorthy_menon_method(R, S)

    print("X = A^-1 = ", end="")
    pprint(X)
    print()
