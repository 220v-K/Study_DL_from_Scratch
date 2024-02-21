# implement XOR GATE using AND, NAND, OR
import numpy as np

# ------- AND, NAND, OR -------

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7    # bias
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # weight and bias are different from AND
    b = 0.7    # weight and bias are different from AND
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])   # weight and bias are different from AND
    b = -0.2    # weight and bias are different from AND
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# ------- XOR -------

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print("- XOR -")
print(XOR(0, 0))  # 0
print(XOR(1, 0))  # 1
print(XOR(0, 1))  # 1
print(XOR(1, 1))  # 0

