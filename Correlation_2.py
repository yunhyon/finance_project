'''
1. Generate N(e.g. 10,000) pairs of two Normal random variables, X and Y. X ~ N(\mu_x, \sigma_x), Y ~ N(\mu_y, \sigma_y).
   (X_1, Y_1), (X_2, Y_2), ... (X_N, Y_N)
2. Calculate correlation from the N pairs of (X,Y). Correlation would be close to zero because X and Y are perfectly uncorrelated.
'''

import random
import math

mu_x = 0.0
mu_y = 0.0
sigma_x = 1.0
sigma_y = 1.0
N = 1000000
X = []
Y = []
for i in range(0, N):
    x = random.normalvariate(mu_x, sigma_x)
    y = random.normalvariate(mu_y, sigma_y)
    X.append(x)
    Y.append(y)

#list comprehension
EX  = sum(X)/N #EX is supposed to be very close to mu_x, which is the true mean
EX2 = sum([ elem*elem for elem in X])/N
EY  = sum(Y)/N
EY2 = sum([ elem*elem for elem in Y ])/N
EXY = sum([ elem_x*elem_y for elem_x,elem_y in zip(X,Y) ])/N


Correlation = (EXY - EX * EY) / ( math.sqrt(EX2 - EX * EX) * math.sqrt(EY2 - EY * EY))
print(Correlation)

'''
E[X] = 1/N*sum(X_1, X_2,...X_N) # estimation of E[X)
E[Y] = 1/N*sum(Y_1, Y_2,...Y_N)
E[X^2] = 1/N*sum(X_1^2, X_2^2,...X_N^2) # estimation of E[X)
E[Y^2] = 1/N*sum(Y_1^2, Y_2^2,...Y_N^2)
E[XY] = 1/N*sum(X_1*Y_1, ..., X_N*Y_N)
correlation = (E[XY] -E[X]E[Y])/{(E[X^2]-E[X]^2)*(E[Y^2]-E[Y]^2)}^0.5
'''


