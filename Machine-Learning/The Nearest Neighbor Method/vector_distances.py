import math
import numpy as np

x_train = np.array([[25, 2, 50, 1, 500], 
                  [39, 3, 10, 1, 1000],    
                  [82, 5, 20, 2, 120], 
                  [130, 6, 10, 2, 600]])
y_train = [127900, 222100,  268000, 460700]

x_test = np.array([[115, 6, 10, 1, 560], [13, 2, 13, 1, 1000]])


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

n_train = len(x_train) # number of data points in the training set

for test_item in x_test:
    d = np.empty(n_train) # d will hold the distances between this test data point and all the training data points
    for i, train_item in enumerate(x_train):
        d[i] = dist(test_item, train_item)
    nearest_index = np.argmin(d) # the nearest neighbour will be in y_train[nearest]
    print(y_train[nearest_index])
