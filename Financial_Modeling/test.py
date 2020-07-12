import pickle
import pandas as pd

'''
pickle file - >list of lists -> pandas dataframe - >csv
'''
corr_mat = pickle.load(open("Correlation_Matrix.p","rb"))
df_corr_mat = pd.DataFrame(corr_mat)
df_corr_mat.to_csv('Correlation_Matrix.csv', index=False)