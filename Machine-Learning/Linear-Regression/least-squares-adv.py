def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = 0
    
    x_and_c = []
    for coeff in c:
        x_and_c.append(X @ coeff)
    x_and_X = np.array(x_and_c)
    coefficient = []
    for i in x_and_X:
        coefficient.append([np.square((n - j)) for n, j in zip(y, i)])
    number = np.sum(coefficient[0])
    for i in coefficient:
        
        if sum(i)<number:
            number = sum(i)
            best_index = coefficient.index(i)


    print("the best set is set %d" % best_index)


find_best(X, y, c)
