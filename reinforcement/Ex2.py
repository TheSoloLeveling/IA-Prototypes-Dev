import numpy as np
import pandas as pd

h = pd.read_csv('Happiness.csv')

rows = h.shape[0]
cols = h.shape[1]
colsName = list(h.columns)

regionsNbr = rows
print("number of rows : ", rows)
print("number of cols  : ",cols)
print("colomns name : ",colsName)

print(h.describe())
h.sort_values(by=['Overall rank'], inplace=True)
print(h[['Overall rank', 'Country or region']])


