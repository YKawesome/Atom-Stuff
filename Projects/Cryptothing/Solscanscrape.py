import pandas as pd #Pandas Database
import numpy as np #Numpy Arrays

import ssl
import xlwt
from xlwt import Workbook
import time
import math
from decimal import *
getcontext().prec = 20
decimal_style = xlwt.XFStyle()
decimal_style.num_format_str = '0.00000000000000000000'

FILENAME='portolasolcsv.xlsx'
df=pd.read_excel(FILENAME,skiprows=[0])

# print('Database\n')
print(df) #Full Database
# print('\nInfo\n')
# print(df.info()) #Database Info, such as Data Type and Non-Null Count
# print('\nColumns\n')
# print(df.columns) #Column Names
# print('\nHead\n')
# print(df.head()) #First 5 Entries
# print('\nTail\n')
# print(df.tail()) #Last 5 Entries
# print('\nShape\n')
# print(df.shape) #Shape of the Matrix

for i, row in df.iterrows():
    if row['received_currency'] in ['MER', 'MNDE', 'SBR', 'SUNNY', 'ORCA']:
        df.at[i,'tx_type'] = "Mining Reward"
    if str(row['received_currency'])[:3] in ['SRY','iou']:
        df.at[i,'tx_type'] = "Fee"
        print('done')
print(df.iat[223,1])

# for timestamp, trantype, taxtable, buy, buyc, sell, sellc, fee, feec, comment, txid, url, exchange, wallet in df.iterrows():
#     print(timestamp)
