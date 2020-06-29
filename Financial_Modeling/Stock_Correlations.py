import pandas as pd
import numpy as np
import statsmodels.api as sm
import math


df_training_data = pd.read_csv('training.csv')
def rho(i, j):
    '''
    :param i: stock_i column, ex) i=1 means the column with the name 'stock_1', 1 <= i <= 500
    :param j: stock_j column, ex) j=1 means the column with the name 'stock_1', 1 <= j <= 500
    :return: correlation between the stock_i column and stock_j column
    '''
    if i < 1 or i > 500:
        raise("i should be in the interval of 1 and 500 inclusive")
    if j < 1 or j > 500:
        raise("j should be in the interval of 1 and 500 inclusive")
    array_i = df_training_data[df_training_data.columns.values[i-1]]
    array_j = df_training_data[df_training_data.columns.values[j-1]]
    N   = 1./4000.
    Ei  = sum(array_i)*N
    Ej  = sum(array_j)*N
    Ei2 = sum([elem*elem for elem in array_i])*N
    Ej2 = sum([elem*elem for elem in array_j])*N
    Eij = sum([elem_i*elem_j for elem_i, elem_j in zip(array_i, array_j)]) * N
    return (Eij - Ei * Ej)/(math.sqrt(Ei2 - Ei * Ei) * math.sqrt(Ej2 - Ej * Ej))

print(rho(1,2)) # This number should be -0.8710786026729423

def upper_triangular_matrix(size):
    upper_triangular_matrix = []
    for i in range(1, size+1):
        print(i)
        inner_matrix = []
        for j in range(i + 1, size+1):
            inner_matrix.append(rho(i, j))
        upper_triangular_matrix.append([1.0] + inner_matrix)
    return upper_triangular_matrix

def correlation_matrix(upper_triangular_matrix):
    for i in range(1,len(upper_triangular_matrix)):
        for j in range(0,i):
            [upper_triangular_matrix[j][i-1]]+upper_triangular_matrix[i]
    return upper_triangular_matrix

ut_matrix = upper_triangular_matrix(5)
corr_matrix = correlation_matrix(ut_matrix)
print(corr_matrix)




