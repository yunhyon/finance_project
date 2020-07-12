'''
We generate a series of data (X,Y) as follows
Y = 1*1+0.1*X + e(normal random variables)
Then, we use Linear Regression(an OLS) to best estimate the parameters a,b,c to minimize the sum of the squared errors.
Y_estimated = a*1 + b*X  #OLS is trying to find the best a, b  which minimizes the sum of squared errors
'''

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.sandbox.regression.predstd as pred

nsample = 100
x = np.linspace(0, 10, 100)
X = np.column_stack((x,))
beta = np.array([1, 0.1])
e = np.random.normal(size = nsample)

# Now we generate a data set of X and Y to be analyzed by OLS(Ordinary Least Squares)
X_value = sm.add_constant(X)
Y_value = np.dot(X_value, beta) + e

model = sm.OLS(Y_value, X_value)
results = model.fit()
print(results.summary())

