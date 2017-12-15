import numpy as np
import json
from random import uniform


def generate_matrices():
    matrices = {}
    for matrixSize in range(2, 501):  # to create 2x2, 3x3, ... , 500x500 square matrices
        A = np.array([[uniform(1, 100) for _ in range(matrixSize)] for _ in range(matrixSize)])
        A = np.dot(A, A.transpose()).tolist()
        matrices[matrixSize] = A
    return matrices


def write_to_json(to_write):
    filename = "data.json"
    with open(filename, 'w') as f:
        json.dump(to_write, f)


def main():
    data = generate_matrices()
    write_to_json(data)
