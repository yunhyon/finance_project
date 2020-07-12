'''
The S&P 500 index is an American stock market based on the market capitalization of 500 large companies
that have common stock listed on the NYSE or NASDAQ. 4,000 values, collected in a minute, for 500 stocks
will be used to train a model that predicts future values of the S&P 500 index based on linear regression.
'''

import pandas as pd
import numpy as np
import statsmodels.api as sm

df_training_data = pd.read_csv('training.csv')

'''
Here, the stock values are being converted from type "np.ndarray" to type "list" to type "tuple". This is so 
the list is usable by the "sm.OLS" command, which will calculate the best coefficients of the linear regression
model to minimize the error. 
'''
array_list = []
for elem in list(df_training_data.columns.values)[0:-1]:
    x = df_training_data[elem].values[0:3000]
    array_list.append(x)

array_list.append(pd.array([1.0]*3000))
tuple(array_list)
X_value = np.column_stack(tuple(array_list))
#X_value = sm.add_constant(X)
Y_value = df_training_data['S&P500'].values[0:3000]
'''
The linear regression model is: the square of the model index from the true index. The true index value is the Y_value 
and the model index is calculated by the a combination of the stock values and their respective coefficients, as mentioned
before.
'''

model = sm.OLS(Y_value, X_value)
results = model.fit()
print(results)

New_Y_value = df_training_data['S&P500'].values[2999:4002]
New_Y_value.tolist()
params_list = results.params.tolist()

error_list = []
model_value_list = []
for Y_True, ii in zip(New_Y_value, range(1000)):
    stock_price_row = df_training_data.loc[ii].tolist()[3001:4002]
    relative_error = abs( ( Y_True - (np.dot(stock_price_row, params_list[0:-1]) + params_list[-1]) )/Y_True )*100  #(Y_True-(a_1*S_1+...+a_500*s_500+a_501)/Y_True
    error_list.append(relative_error)
    model_value_list.append(np.dot(stock_price_row, params_list[0:-1]) + params_list[-1])
print(error_list)
print(New_Y_value)
print(model_value_list)



# Create OLS_4.py and train the model only with first 3000 data in training.csv.
# Then test the model performance as above with the rest 1000 data. This test is called out-of sample test.