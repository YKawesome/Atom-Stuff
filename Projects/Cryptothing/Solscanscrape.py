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
headerdone = False
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

wb = Workbook()
cSheet = wb.add_sheet('Crypto Data')
def writeToExcelFile(number, datep, timep, walletp, typetranp, buycurrencyp, buyunitsp, sellcurrencyp, sellunitsp, feecurrencyp, feeunitsp, urlp):
    # datalist = [datep, timep, walletp, typetranp, buyunitsp, Decimal(buycurrencyp), sellunitsp, Decimal(sellcurrencyp), feecurrencyp, Decimal(feeunitsp), urlp]
    datalist = [datep, timep, walletp, typetranp, buyunitsp, buycurrencyp, sellunitsp, sellcurrencyp, feecurrencyp, feeunitsp, urlp]

    global headerdone
    if headerdone:
        # try:
        #     if datalist[5] != None:
        #         datalist[5] = Decimal(datalist[5])
        #     if datalist[7] != None:
        #         datalist[7] = Decimal(datalist[7])
        #     if datalist[9] != None:
        #         datalist[9] = Decimal(datalist[9])
        # except:
        #     print('moving on')
        pass
    else:
        headerdone = True
    for index, item in enumerate(datalist):
        cSheet.write(number, index, item, decimal_style)
writeToExcelFile(0, 'Date', 'Time Stamp', 'Exchange/Wallet Name', 'Type of Transaction (Transfer/Trade/Mining)', 'Buy Units', 'Buy Currency (Use USD or Ticker as per coinmarketcap.com)', 'Sell Units', 'Sell Currency (Use USD or Ticker as per coinmarketcap.com)', 'Fee Currency(if applicable or not netted into buy/sell amount)', 'Fee Units (if applicable or not netted into buy/sell amount)', 'URL')

df = df.loc[::-1, :]
print(df)
for i, row in df.iterrows():
    # Rename some stuff
    if row['received_currency'] in ['MER', 'MNDE', 'SBR', 'SUNNY', 'ORCA']:
        df.at[i,'tx_type'] = "Mining Reward"
    if str(row['received_currency'])[:3] in ['SRY','iou']:
        df.at[i,'tx_type'] = "Fee"
    if row['received_currency'] in ['USDT', 'USDC']:
        df.at[i, 'tx_type'] = "Trade"

for index, (i, row) in enumerate(df.iterrows()):

    #start writing
    date = row[0].split(' ')[0]
    timestamp = row[0].split(' ')[1]


    if row[1] == 'Mining Reward':
        writeToExcelFile(index+1, date, timestamp, "Ledger-Solana - Ayad", row[1], row[3], row[4], None, None, "SOL", 0.000005, row[11])

    if row[1] == "Fee":
        writeToExcelFile(index+1, date, timestamp, "Ledger-Solana - Ayad", row[1], None, None, None, None, "SOL", row[7], row[11])

    # if row[1] == "Trade":
    #     writeToExcelFile(index+1, date, timestamp, "Ledger-Solana - Ayad", row[1], None, None, None, None, "SOL", row[7], row[9])

# for index, row in df.iterrows():


# timestamp, trantype, taxtable, buy, buyc, sell, sellc, fee, feec, comment, txid, url, exchange, wallet
wb.save('solscrapeone.xlsx')
