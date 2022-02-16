import pandas as pd #Pandas Database
import numpy as np #Numpy Arrays
FILENAME='portolasolcsv.xlsx'
df=pd.read_excel(FILENAME,skiprows=[0])

print('Database\n')
print(df) #Full Database
print('\nInfo\n')
print(df.info()) #Database Info, such as Data Type and Non-Null Count
print('\nColumns\n')
print(df.columns) #Column Names
print('\nHead\n')
print(df.head()) #First 5 Entries
print('\nTail\n')
print(df.tail()) #Last 5 Entries
print('\nShape\n')
print(df.shape) #Shape of the Matrix
