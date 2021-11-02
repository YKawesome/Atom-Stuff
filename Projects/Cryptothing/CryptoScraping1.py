from selenium import webdriver
from decimal import *
getcontext().prec = 25
# pip install webdriver-manager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xlwt
from xlwt import Workbooks

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://blockscout.moonriver.moonbeam.network/address/0x66fB1cD65b97fa40457b90b7d1ca6B92Cb64b32b/transactions")


time.sleep(7)
c = int(driver.find_elements(By.XPATH, "//*[@data-selector='transaction-count']")[0].get_attribute('innerHTML').strip().split(' ')[0])
pages = math.ceil(c/50)
clicks = pages-1

a = driver.find_elements(By.CLASS_NAME, "text-truncate")
b = driver.find_elements(By.CLASS_NAME, "bs-label")
linklist = list()
counter = 0
for thing in a:
    linklist.append((thing.get_attribute('href'),b[counter].get_attribute('innerHTML').strip()))
    counter+=1

for click in range(clicks):
    python_button = driver.find_elements(By.CLASS_NAME, "page-link")[3]
    python_button.click()
    time.sleep(4)
    a = driver.find_elements(By.CLASS_NAME, "text-truncate")
    b = driver.find_elements(By.CLASS_NAME, "bs-label")
    counter = 0
    for thing in a:
        linklist.append((thing.get_attribute('href'),b[counter].get_attribute('innerHTML').strip()))
        counter+=1


driver.quit()

# linklist= [('https://blockscout.moonriver.moonbeam.network/tx/0x0320272492f261cc411244e17fbc53dff1d114afed89a5b8afa96e20fc205840', 'Deposit')]

wallet = '0x828d9957e93FEfe1D501D692eA2186d682eA5E4a'

def namer(list):
    for index, (url, tratype) in enumerate(list):
        if tratype == "AddLiquidityETH":
            list[index] = (url, "Stake (LP)e")
        elif tratype == "SwapExactTokensForETH":
            list[index] = (url, "TradeE")
        elif tratype == "SwapTokensForExactTokens":
            list[index] = (url, "TradeF")
        elif tratype == "SwapExactETHForTokens":
            list[index] = (url, "TradeG")
        elif tratype == "SwapExactTokensForTokens":
            list[index] = (url, "TradeH")
        elif tratype == "AddLiquidity":
            list[index] = (url, "Stake (LP)o")
        elif tratype == "Deposit":
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, "html.parser")
                result = soup.find_all("h3", {"class" : "address-balance-text"})
                if len(result) == 3 or len(result)==2:
                    list[index] = (url, "Mining Reward")
                else:
                    list[index] = (url, "Stake")
        else:
            list[index] = (url, tratype)

namer(linklist)


wb = Workbook()
cSheet = wb.add_sheet('Crypto Data')

def writeToExcelFile(number, datep, timep, walletp, typetranp, buycurrencyp, buyunitsp, sellcurrencyp, sellunitsp, feecurrencyp, feeunitsp, urlp):
    datalist = [datep, timep, walletp, typetranp, buyunitsp, Decimal(buycurrencyp), sellunitsp, Decimal(sellcurrencyp), feecurrencyp, Decimal(feeunitsp), urlp]
    for index, item in enumerate(datalist):
        cSheet.write(number, index, item)
writeToExcelFile(0, 'Date', 'Time Stamp', 'Exchange/Wallet Name', 'Type of Transaction (Transfer/Trade/Mining)', 'Buy Units', 'Buy Currency (Use USD or Ticker as per coinmarketcap.com)', 'Sell Units', 'Sell Currency (Use USD or Ticker as per coinmarketcap.com)', 'Fee Currency(if applicable or not netted into buy/sell amount)', 'Fee Units (if applicable or not netted into buy/sell amount)', 'URL')


linklist.reverse()
counteroflps=0
for index, (url, tratype) in enumerate(linklist):
    if tratype == "Stake":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        sell = result[0].text.strip().split(' ')
        buy = result[1].text.strip().split(' ')

        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsv = fee[0].strip()
        feecurrencyv = fee[1].strip()
        sellunitsv = sell[1].strip()
        sellcurrencyv = sell[0].strip()
        buyunitsv = buy[1].strip()
        buycurrencyv = buy[0].strip()

        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, tratype, buycurrencyv, buyunitsv, sellcurrencyv, sellunitsv, feecurrencyv, feeunitsv, url)
    elif tratype == "TradeE" or tratype == "TradeG" or tratype == "TradeH":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        sell = result[0].text.strip().split(' ')
        buy = result[1].text.strip().split(' ')


        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsv = fee[0].strip()
        feecurrencyv = fee[1].strip()
        sellunitsv = sell[1].strip()
        sellcurrencyv = sell[0].strip()
        buyunitsv = buy[1].strip()
        buycurrencyv = buy[0].strip()
        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, "Trade", buycurrencyv, buyunitsv, sellcurrencyv, sellunitsv, feecurrencyv, feeunitsv, url)

    elif tratype == "TradeF":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        sell = result[2].text.strip().split(' ')
        buy = result[0].text.strip().split(' ')


        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsv = fee[0].strip()
        feecurrencyv = fee[1].strip()
        sellunitsv = sell[1].strip()
        sellcurrencyv = sell[0].strip()
        buyunitsv = buy[1].strip()
        buycurrencyv = buy[0].strip()
        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, "Trade", buycurrencyv, buyunitsv, sellcurrencyv, sellunitsv, feecurrencyv, feeunitsv, url)

    elif tratype == "Stake (LP)e":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        selltwo = result[0].text.strip().split(' ')
        sellone = result[1].text.strip().split(' ')
        buy = result[3].text.strip().split(' ')



        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsonev = fee[0].strip()
        feecurrencyonev = fee[1].strip()
        feeunitstwov = 0
        feecurrencytwov = feecurrencyonev
        buyunitsv = buy[1].strip()
        buycurrencyv = buy[0].strip()
        sellunitsonev = sellone[1].strip()
        sellcurrencyonev = sellone[0].strip()
        sellunitstwov = selltwo[1].strip()
        sellcurrencytwov = selltwo[0].strip()

        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, "Stake (LP)", buycurrencyv, buyunitsv, sellcurrencyonev, sellunitsonev, feecurrencyonev, feeunitsonev, url)
        writeToExcelFile(index+2+counteroflps, datev, timev, wallet, "Stake (LP)", None, None, sellcurrencytwov, sellunitstwov, feecurrencytwov, feeunitstwov, url)

        counteroflps+=1

    elif tratype == "Stake (LP)o":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')

        result = soup.find_all("span", {"data-transaction-status" : "Error: execution reverted"})

        if len(result) == 1:
            selltwo=None
            sellone=None
            buyunitsv = None
            buycurrencyv = None
            sellunitsonev = None
            sellcurrencyonev = None
            sellunitstwov = None
            sellcurrencytwov = None
        else:
            result = soup.find_all("h3", {"class" : "address-balance-text"})
            selltwo = result[1].text.strip().split(' ')
            sellone = result[0].text.strip().split(' ')
            buy = result[2].text.strip().split(' ')
            buyunitsv = buy[1].strip()
            buycurrencyv = buy[0].strip()
            sellunitsonev = sellone[1].strip()
            sellcurrencyonev = sellone[0].strip()
            sellunitstwov = selltwo[1].strip()
            sellcurrencytwov = selltwo[0].strip()



        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsonev = fee[0].strip()
        feecurrencyonev = fee[1].strip()
        feeunitstwov = 0
        feecurrencytwov = feecurrencyonev


        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, "Stake (LP)", buycurrencyv, buyunitsv, sellcurrencyonev, sellunitsonev, feecurrencyonev, feeunitsonev, url)
        writeToExcelFile(index+2+counteroflps, datev, timev, wallet, "Stake (LP)", None, None, sellcurrencytwov, sellunitstwov, feecurrencytwov, feeunitstwov, url)

        counteroflps+=1

    elif tratype == "Mining Reward":
        #start here
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        buy = result[0].text.strip().split(' ')



        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsv = fee[0].strip()
        feecurrencyv = fee[1].strip()
        buyunitsv = buy[1].strip()
        buycurrencyv = buy[0].strip()

        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, tratype, buycurrencyv, buyunitsv, None, None, feecurrencyv, feeunitsv, url)

    elif tratype == "Withdraw":
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')
        result = soup.find_all("h3", {"class" : "address-balance-text"})
        buyone = result[1].text.strip().split(' ')
        buytwo = result[0].text.strip().split(' ')



        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsonev = fee[0].strip()
        feecurrencyonev = fee[1].strip()
        feeunitstwov = 0
        feecurrencytwov = feecurrencyonev
        buyunitsonev = buyone[1].strip()
        buycurrencyonev = buyone[0].strip()
        buyunitstwov = buytwo[1].strip()
        buycurrencytwov = buytwo[0].strip()

        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, "Withdraw", buycurrencyonev, buyunitsonev, None, None, feecurrencyonev, feeunitsonev, url)
        writeToExcelFile(index+2+counteroflps, datev, timev, wallet, "Withdraw", buycurrencytwov, buyunitstwov, None, None, feecurrencytwov, feeunitstwov, url)

        counteroflps+=1

    else:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find_all("span", {"class" : "mr-4"})
        dated = result[2].select('span:first-child')[0]['data-from-now'].split(' ')
        result = soup.find_all("dd", {"class" : "col-sm-9"})
        fee = result[3].text.split(' ')



        datev = dated[0]
        timev = dated[1]
        urlv = url
        feeunitsv = fee[0].strip()
        feecurrencyv = fee[1].strip()

        writeToExcelFile(index+1+counteroflps, datev, timev, wallet, tratype, None, None, None, None, feecurrencyv, feeunitsv, url)





wb.save('cryptoscrapingone.xlsx')
