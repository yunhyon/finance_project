import random
import math

mu = 10.0 # mean of X
sigma = 2.0
N = 1000000
rho = -0.7

X = []
Y = []
for i in range(0, N):
    x = random.normalvariate(mu, sigma)
    z = random.normalvariate(mu, sigma) # X and Z are perfectly uncorrelated
    x3 = random.normalvariate(mu, sigma)
    #y = z
    y = rho*x + math.sqrt(1-rho*rho)*z  # X and Y are correlated with rho. Y is still normal random variable.
    X.append(x)
    Y.append(y)

#list comprehension
EX  = sum(X)/N # this is the measurement of mu_x by sampling X N times.
EX2 = sum([ elem*elem for elem in X])/N
EY  = sum(Y)/N
EY2 = sum([ elem*elem for elem in Y ])/N
EXY = sum([ elem_x*elem_y for elem_x,elem_y in zip(X,Y) ])/N


Correlation = (EXY - EX * EY) / ( math.sqrt(EX2 - EX * EX) * math.sqrt(EY2 - EY * EY)) #rho measured  by sampling
print(Correlation)
