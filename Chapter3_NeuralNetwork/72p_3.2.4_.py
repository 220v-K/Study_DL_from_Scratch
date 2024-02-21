# Implement Sigmoid function

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x = np.array([-1.0, 1.0, 2.0])
# print(sigmoid(x))  # [0.26894142 0.73105858 0.88079708]

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y축 범위 지정
plt.show()