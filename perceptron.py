import numpy as np


def activation(equation):

    sigmoid = 1/(1 + np.exp(-(equation)))
    return sigmoid

def perceptron(feature: list, weight: list):

    feature_arr = np.array(feature)
    weight_arr = np.array(weight)

    weight_arr_transpose = np.transpose(weight_arr)
    perceptron_eq = np.dot(feature_arr, weight_arr_transpose)

    result = activation(equation=perceptron_eq)
    print(result)

    if result > 0.5:
        return 1
    return 0


f = [1,2,3,4,5]
w = [5,6,7,8,9]

print(perceptron(feature=f, weight=w))