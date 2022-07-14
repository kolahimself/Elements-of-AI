import numpy as np

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    x_train = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
        ]
    )   
    
    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    # add the feature data for the two new cabins here. note: don't include the price data
    x_test = np.array(
        [
            [36, 3, 15, 1, 850],
            [75, 5, 18, 2, 540]
        ]
    )

    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    # this will print the predicted prices for the six cabins in the training data
    # change this so that it predicts the prices of the two new cabins that are not
    # included in the training set

    print(x_test @ c)

main()
