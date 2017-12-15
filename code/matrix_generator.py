import numpy as np
import json
from random import uniform



matrices = {}
for matrixSize in range(2,501): # to create from 2x2, 3x3, .., 1000x1000 matrices
    A = np.array([[uniform(1,100) for _ in range(matrixSize)] for _ in range(matrixSize)])
    A = np.dot(A,A.transpose()).tolist()
    matrices[matrixSize] = A




filename = "data.json"
with open(filename, 'w') as f:
    json.dump(matrices, f)


# pprint(dik)

