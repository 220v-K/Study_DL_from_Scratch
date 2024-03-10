import sys, os
sys.path.append(os.getcwd())
import numpy as np
from resources.mnist import load_mnist
from functions import sigmoid, softmax

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)