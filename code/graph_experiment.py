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
    # return ave
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

# file1 = open('y1', 'w')
#
# file2 = open('y2', 'w')
#
# file3 = open('y3', 'w')
#
# file4 = open('x', 'w')

print("start")

for i in range(2, n, 1):
    result_x = [log10(x) for x in range(2, i+1, 1)]
    A = data[str(i)]
    print("matrix of size " + str(i))

    # krishnamoorthy_menon_method
    t1 = test(matrix_inversion_cholesky, A)
    result_y.append(log10(t1[0]))
    result1_y_ave.append(log10(t1[1]))
    # file1.write(str(t1) + "\n")

    # test1
    t2 = test(test1, A)
    result2_y.append(log10(t2[0]))
    result2_y_ave.append(log10(t2[1]))
    # file2.write(str(t2) + "\n")

    # test2
    t3 = test(test2, A)
    result3_y.append(log10(t3[0]))
    result3_y_ave.append(log10(t3[1]))

    y1 = result_y  # krishnamoorthy_menon_method
    y2 = result2_y
    y3 = result3_y
    x = result_x

    # file1.close()
    # file2.close()
    # file3.close()
    # file4.close()

    # plt.plot(x, y)
    fig, ax = plt.subplots(figsize=(10, 6))

    plt.plot(x, y1, 'r', label='krishnamoorthy_menon_method (Mode)')  # plotting t, a separately
    plt.plot(x, result1_y_ave, 'r--', label='krishnamoorthy_menon_method (Average)')
    plt.plot(x, y2, 'b', label='numpy.linalg.inv (Mode)')  # plotting t, b separately
    plt.plot(x, result2_y_ave, 'b--', label='numpy.linalg.inv (Average)')
    plt.plot(x, y3, 'g', label='gauss_jordan_elimination (Mode)')  # plotting t, c separately
    plt.plot(x, result3_y_ave, 'g--', label='gauss_jordan_elimination (Average)')
    # xmarks=x
    # plt.xticks(xmarks)
    plt.xlabel('size of a matrix, lg(n)')
    plt.ylabel('time, lg(s)')
    # plt.title('Time and size of a matrix')
    # plt.grid(True)
    plt.legend()

    plt.savefig("../experiments/" + str(i) + "max_matrix.size.png")

    # file3.write(str(t3) + "\n")

    # file4.write(str(i) + "\n")
    # print("t1 =", t1)
    # print("t2 =", t2)
    # print("t3 =", t3)
    # input()
    # input()

# print("ave =", ave)
#
# trials_min = min(trials)
# trials_max = max(trials)

# plt.hist(trials, bins=np.arange(trials_min, trials_max, 0.025))
# from scipy import stats
#
# m = stats.mode(trials)
#
# plt.text(2.5, 500, 'Mode = ' + str(m[0][0]))

# print(trials)

# mpl.style.use('seaborn')

# plt.plot(trials, [1], 'C1', label='C1')

y1 = result_y  # krishnamoorthy_menon_method
y2 = result2_y
y3 = result3_y
x = result_x

# file1.close()
# file2.close()
# file3.close()
# file4.close()

# plt.plot(x, y)
fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(x, y1, 'r', label='krishnamoorthy_menon_method (Mode)')  # plotting t, a separately
plt.plot(x, result1_y_ave, 'r--', label='krishnamoorthy_menon_method (Average)')
plt.plot(x, y2, 'b', label='numpy.linalg.inv (Mode)')  # plotting t, b separately
plt.plot(x, result2_y_ave, 'b--', label='numpy.linalg.inv (Average)')
plt.plot(x, y3, 'g', label='gauss_jordan_elimination (Mode)')  # plotting t, c separately
plt.plot(x, result3_y_ave, 'g--', label='gauss_jordan_elimination (Average)')
# xmarks=x
# plt.xticks(xmarks)
plt.xlabel('size of a matrix, lg(n)')
plt.ylabel('time, lg(s)')
# plt.title('Time and size of a matrix')
# plt.grid(True)
plt.legend()

plt.show()
