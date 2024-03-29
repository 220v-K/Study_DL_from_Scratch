import numpy as np

def step_function(x):
    return np.array(x > 0, dtype=int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # to prevent overflow
    sum_exp_a = np.sum(exp_a)
    y = exp_a = sum_exp_a
    
    return y

def MSE(y, t):  # Mean Squared Error
    return 0.5 * np.sum((y-t)**2)

def CEE(y, t):  # Cross Entropy Error
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))