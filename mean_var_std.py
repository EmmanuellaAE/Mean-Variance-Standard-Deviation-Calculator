#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing Libraries

import numpy as np
import pandas as pd


# In[11]:


# Creating a list of 9 digits.

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

calculate([19, 23, 22, 13, 25, 19, 8, 28, 14])
    
    


# In[24]:





# In[ ]:




