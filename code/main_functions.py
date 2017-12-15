from math import sqrt


def cholesky(A):
    """
    Cholesky decomposition

    :param A: 2D matrix for decomposing
    :return: lower triangular 2D matrix L, part of the decomposition A = L*L^T = R^T*R

    >>> cholesky([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
    [[2.0, 0.0, 0.0], [6.0, 1.0, 0.0], [-8.0, 5.0, 3.0]]

    """
    n = len(A)

    L = [[0.0] * n for _ in range(0, n, 1)]

    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            tmp_sum = 0
            for k in range(0, j, 1):
                tmp_sum += L[i][k] * L[j][k]
            if i == j:  # Diagonal elements
                L[i][j] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - tmp_sum))
    return L


def transpose(a):
    """
    Matrix transposition

    :param a: 2D matrix for transposition
    :return: transposed 2D matrix a^T

    >>> transpose([[2.0, 0.0, 0.0], [6.0, 1.0, 0.0], [-8.0, 5.0, 3.0]])
    [[2.0, 6.0, -8.0], [6.0, 1.0, 5.0], [-8.0, 5.0, 3.0]]

    """

    n = len(a)
    # matrix_transpose = deepcopy(a)
    matrix_transpose = a
    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            matrix_transpose[j][i] = a[i][j]
    return matrix_transpose


def intermediate_diagonal_inverse_matrix(r):
    """
    Create intermediate diagonal matrix for Krishnamoorthy-menon method

    :param r:
    :return:

    >>> intermediate_diagonal_inverse_matrix([[2.0, 6.0, -8.0], [6.0, 1.0, 5.0], [-8.0, 5.0, 3.0]])
    [[0.5, 0, 0], [0, 1.0, 0], [0, 0, 0.3333333333333333]]
    """
    n = len(r)
    S = [[0] * n for i in range(1, n + 1, 1)]
    for i in range(0, n, 1):
        S[i][i] = 1 / r[i][i]
    return S


def krishnamoorthy_menon_method(R, S):
    """
    Krishnamoorthy-menon method - proposed method for the problem

    R*x_i = s_i

    :param R:
    :param S:
    :return:
    """
    n = len(R)
    X = [[0.0] * n for i in range(0, n, 1)]

    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            tmp_sum = 0
            for k in range(j + 1, n, 1):
                tmp_sum += R[j][k] * X[k][i]
            X[j][i] = (S[j][i] - tmp_sum) / R[j][j]
            X[i][j] = X[j][i]
    return X
