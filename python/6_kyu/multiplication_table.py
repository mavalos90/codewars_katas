# Multiplication table
# 6 kyu

'''
Your task, is to create NxN multiplication table, of size provided in parameter.
For example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''

# With List Comprehension

def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

# With numpy:

import numpy as np
def multiplication_table(size):
    table = np.zeros(shape=(size, size))
    table[0] = list(range(1,size+1))
    for i in range(1, size):
        table[i] = table[0] * (i+1)
    return table.tolist()