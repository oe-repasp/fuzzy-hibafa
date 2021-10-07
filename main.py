


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
print("1")

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([0, 1, 1, 0])

plt.plot(ypoints, linestyle = 'dotted', color = 'r')


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
