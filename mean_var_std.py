# Importing Numpy Library

import numpy as np

# Creating a function that returns aggregates of nine numbers.

def calculate(nine_int):
    if len(nine_int) != 9:
        raise ValueError("List must contain nine numbers")
    else:
        matrix = np.reshape(nine_int, (3, 3))

    aggregates = {'mean:': [np.mean(matrix, axis =0, dtype='float16').tolist(),
                 np.mean(matrix, axis= 1, dtype= 'float16').tolist(), np.mean(matrix, dtype='float16')],
    'variance:' : [np.var(matrix, axis= 0, dtype= 'float16').tolist(), np.var(matrix, axis= 1, dtype= 'float16').tolist(),
                     np.var(matrix, dtype='float16')],
    'standard_deviation:' : [np.std(matrix, axis=0, dtype='float16').tolist(),
                                np.std(matrix, axis= 1, dtype='float16').tolist(),np.std(matrix, dtype= 'float16')],
    'max_mat:' :  [np.max(matrix, axis= 0,).tolist(), np.max(matrix, axis= 1).tolist(), np.max(matrix)],
    'min_mat:' : [np.min(matrix, axis= 0).tolist(), np.min(matrix, axis= 1).tolist(), np.min(matrix)],
    'sum_mat:' : [np.sum(matrix, axis= 0).tolist(), np.sum(matrix, axis= 1).tolist(), np.sum(matrix)]
    }
    
    for key,value in aggregates.items():
        print(key,value,'\n')

calculate()
