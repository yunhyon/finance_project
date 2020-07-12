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

A = np.array(corr_mat)
C = np.linalg.cholesky(A)
make_csv(C, 'Cholesky')
CT = np.transpose(C)
make_csv(CT, 'Cholesky_Transpose')
P = np.matmul(C, CT)
make_csv(P, 'Correlation_Matrix')



delta_t = 0.01
start = 0
end = 10.0

for j in range(30):
    t_value = [0.0]
    W_value = [0.0]  # by definition of Brownian motion, W(0) = 0
    W_current = 0.0  # W(0)
    for i in range(1,1001): #the simulation starts from W(0.01)
        t = start + i*delta_t
        t_value.append(t)
        X = random.normalvariate(0.0, math.sqrt(delta_t)) # Generating independent Normal random variable, N(0, 0.01)
        #print(t, W_current, Z)
        W_current = W_current + Z # By definition of BM, W(0.01) = W(0) + Z1(0,0.01), W(0.02) = W(0.01) + Z2(0,0.01),..., W(10) = W(9.99)+ Z1000(0,0.01)
        W_value.append(W_current) # W(t+delta_t) = W(t) + Z(0,0.1)

    plt.plot(t_value,W_value)
plt.show()