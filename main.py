


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
print("1")

import matplotlib.pyplot as plt
import numpy as np
import random

# ypoints = np.array([0, 1, 1, 0])
#
# plt.plot(ypoints, linestyle = 'dotted', color = 'r')

### kek
xpoints = np.array([0,1,2,3,4,5,6])
ypoints = np.array([0,random.random(),random.random(),random.random(),random.random(),random.random(),0])
plt.plot(xpoints,ypoints,color='b')

### piros
xpoints = np.array([0,1,2,3,4,5,6])
ypoints = np.array([0,random.random(),random.random(),random.random(),random.random(),random.random(),0])
plt.plot(xpoints,ypoints,color='r')

### piros
xpoints = np.array([0,1,2,3,4,5,6])
ypoints = np.array([0,random.random(),random.random(),random.random(),random.random(),random.random(),0])
plt.plot(xpoints,ypoints,color='green')




plt.show()
