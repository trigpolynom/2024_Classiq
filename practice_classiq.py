# import classiq
import numpy as np
import matplotlib.pyplot as plt
# classiq.authenticate()

# from classiq import *


# @qfunc
# def main(x: Output[QNum], y: Output[QNum]):

#     allocate(3, x)
#     hadamard_transform(x)  # creates a uniform superposition
#     y |= x**2 + 1

# quantum_program = synthesize(create_model(main))
# show(quantum_program)


def linear_func(a, b, x):
    y = 0
    y |= a*x+b
    return y  

def f(x):
    return np.tanh(x)

x = np.linspace(0, 1, 100)

plt.figure()
# plt.plot(x, linear_func(0.5, 1.5, x))
plt.plot(x, f(x))
plt.show()