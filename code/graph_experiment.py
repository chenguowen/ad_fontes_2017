import matplotlib.pyplot as plt
import numpy as np
import matrix_inversion_cholesky
import test1
import test2
import time
from math import log10
from scipy import stats
import json
from pprint import pprint


def test(f, A):
    trials = []
    for _ in range(0, 1000):
        start = time.time()
        f.main(A)
        t = (time.time() - start)  # * 10 ** 5
        trials.append(t)
    ave = sum(trials) / len(trials)
    m = stats.mode(trials)
    return m[0][0], ave


data = json.load(open('../data/data.json'))

n = 110

result_y = []
result1_y_ave = []
result2_y = []
result2_y_ave = []
result3_y = []
result3_y_ave = []


print("start")

for i in range(2, n, 1):
    result_x = [log10(x) for x in range(2, i+1, 1)]
    A = data[str(i)]
    print("matrix of size " + str(i))

    # krishnamoorthy_menon_method
    t1 = test(matrix_inversion_cholesky, A)
    result_y.append(log10(t1[0]))
    result1_y_ave.append(log10(t1[1]))

    # test1
    t2 = test(test1, A)
    result2_y.append(log10(t2[0]))
    result2_y_ave.append(log10(t2[1]))

    # test2
    t3 = test(test2, A)
    result3_y.append(log10(t3[0]))
    result3_y_ave.append(log10(t3[1]))

    y1 = result_y  # krishnamoorthy_menon_method
    y2 = result2_y
    y3 = result3_y
    x = result_x

    fig, ax = plt.subplots(figsize=(10, 6))

    plt.plot(x, y1, 'r', label='krishnamoorthy_menon_method (Mode)')  # plotting t, a separately
    plt.plot(x, result1_y_ave, 'r--', label='krishnamoorthy_menon_method (Average)')
    plt.plot(x, y2, 'b', label='numpy.linalg.inv (Mode)')  # plotting t, b separately
    plt.plot(x, result2_y_ave, 'b--', label='numpy.linalg.inv (Average)')
    plt.plot(x, y3, 'g', label='gauss_jordan_elimination (Mode)')  # plotting t, c separately
    plt.plot(x, result3_y_ave, 'g--', label='gauss_jordan_elimination (Average)')
    plt.xlabel('size of a matrix, lg(n)')
    plt.ylabel('time, lg(s)')
    plt.legend()

    plt.savefig("../experiments/" + str(i) + "max_matrix.size.png")