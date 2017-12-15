import matplotlib.pyplot as plt
import numpy as np
import matrix_inversion_cholesky
import time

trials = []

# for trial_index in range(0, 1000):
#     start = time.time()
#     main()
#     (time.time() - start) * 10 ** 5  # 1/100000 of a second
# # print(trials)

for _ in range(0, 10000):
    start = time.time()
    matrix_inversion_cholesky.main()
    t = (time.time() - start) * 10 ** 5
    if t > 4:
        continue
    trials.append(t)  # 1/100000 of a second
print(trials)

ave = sum(trials) / len(trials)
print("ave =", ave)


trials_min = min(trials)
trials_max = max(trials)

plt.hist(trials, bins=np.arange(trials_min, trials_max, 0.025))
from scipy import stats

m = stats.mode(trials)

plt.text(2.5, 500, 'Mode = ' + str(m[0][0]))

plt.title("Histogram of time durations for matrix inversion of a 3x3 matrix")
plt.show()
