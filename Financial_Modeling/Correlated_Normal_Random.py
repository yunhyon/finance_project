import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

def make_csv(array, name):
    df = pd.DataFrame(array)
    df.to_csv(name + '.csv', index = False)
    return 0

corr_mat = pickle.load(open("Correlation_Matrix.p","rb"))
df_corr_mat = pd.DataFrame(corr_mat)
df_corr_mat.to_csv('Original_Correlation_Matrix.csv', index=False)

#Checking if A = C*C^T = P
A = np.array(corr_mat)
C = np.linalg.cholesky(A)
make_csv(C, 'Cholesky')
CT = np.transpose(C)
make_csv(CT, 'Cholesky_Transpose')
P = np.matmul(C, CT)
make_csv(P, 'Correlation_Matrix')


current_T = 0.0
delta = 1.0
start = 0.0
delta = 0.01
end = 9.99

current_W = [0.0]*len(C)
current_T = 0.0
T_values = [delta*float(i) for i in range(1000)]  #
W_values = [current_W]  #[ [500 elements], [500 elements],...,[500 elements]]

for i in range(999):
    Z_list = []
    for j in range(len(C)):
        Z_list.append(random.normalvariate(0, (T_values[i+1] - T_values[i])**0.5))
    X_list = np.matmul(C,Z_list)
    current_W = [ W+X for W,X in zip(current_W, X_list) ]
    W_values.append(current_W)

W_values_transposed = [] # [ [1000 elements], [1000 elements] ,... ,[]  ]

for y in range(len(C)):
    w_evolution = []
    for x in range(1000):
        w_evolution.append(W_values[x][y])
    W_values_transposed.append(w_evolution)

plt.plot(T_values, W_values_transposed[2])
plt.plot(T_values, W_values_transposed[5])
plt.show()
