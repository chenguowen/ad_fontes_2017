import matplotlib.pyplot as plt
import numpy as np
import matrix_inversion_cholesky
import time
from scipy import stats


def main():
    trials = []
    A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

    for _ in range(0, 1000):
        start = time.time()
        matrix_inversion_cholesky.main(A)
        t = (time.time() - start) * 10 ** 5
        trials.append(t)  # 1/100000 of a second

    ave = sum(trials) / len(trials)
    m = stats.mode(trials)

    trials_min = min(trials)
    trials_max = max(trials)

    plt.hist(trials, bins=np.arange(trials_min, trials_max, 0.025))

    plt.text(2.5, 100, 'Mode = ' + str(m[0][0]) + '\nAverage = ' + str(ave))
    plt.xlabel('time, 10^-5 s')
    plt.show()
    # plt.savefig("data.png")
