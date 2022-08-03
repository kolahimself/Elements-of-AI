import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def nearest(x_train, x_test):
    rand = []
    
    for eacharray in x_train:
        d = dist(eacharray, x_test)
        rand.append(d)
    
    min_distance  = min(rand)
    nearest = rand.index(min_distance)
    
    return nearest

nearest(x_train, x_test)
