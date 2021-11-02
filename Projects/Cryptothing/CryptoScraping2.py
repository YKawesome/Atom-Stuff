from selenium import webdriver
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
from selenium.common.exceptions import WebDriverException
import urllib.request, urllib.parse, urllib.error
import ssl
import xlwt
from xlwt import Workbook
# (row,column)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://blockscout.moonriver.moonbeam.network/address/0x66fB1cD65b97fa40457b90b7d1ca6B92Cb64b32b/coin-balances")


time.sleep(4)
numberthing = int(driver.find_elements(By.XPATH, "//*[@data-selector='transaction-count']")[0].get_attribute('innerHTML').strip().split(' ')[0])
pages = math.ceil(numberthing/50)
clicks = pages-1

full = driver.find_elements(By.CLASS_NAME, "mt-md-0")
linklist = list()
counter = 0
for index, thing in enumerate(full):
    if (index % 3) == 0:
        linklist.append([])
        linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[-1].get_attribute("data-from-now"))
    if (index % 3) == 1:
        linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[0].text)
    if (index % 3) == 2:
        linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[0].text)
        counter+=1

for click in range(clicks):
    python_button = driver.find_elements(By.CLASS_NAME, "page-link")[3]
    try:
        python_button.click()
        time.sleep(3)
        full = driver.find_elements(By.CLASS_NAME, "mt-md-0")
        for index, thing in enumerate(full):
            if (index % 3) == 0:
                linklist.append([])
                linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[-1].get_attribute("data-from-now"))
            if (index % 3) == 1:
                linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[0].text)
            if (index % 3) == 2:
                linklist[counter].append(thing.find_elements(By.CSS_SELECTOR, "*")[0].text)
                counter+=1
    except WebDriverException:
        print("element is not clickable")
driver.quit()



# print(linklist)


def formatter(list):
    for index, [timestamp,gred,movr] in enumerate(list):
        if gred.split()[0] == "▼":
            list[index][1] = "-" + gred.split()[1] + ' ' + gred.split()[2]
        elif gred.split()[0] == "▲":
            list[index][1] = gred.split()[1] + ' ' + gred.split()[2]
    return list
linklist = formatter(linklist)
# print(linklist)

wb = Workbook()
cSheet = wb.add_sheet('Crypto Data')

def writeToExcelFile(number, datep, timep, greencurrency, redcurrency, othercur):
    datalist = [datep, timep, greencurrency, redcurrency, othercur]
    for index, item in enumerate(datalist):
        cSheet.write(number, index, item)
writeToExcelFile(0, 'Date', 'Time Stamp', 'Green Units', 'Red Units', 'Balance')

linklist.reverse()
for index, [timestamp,gred,movr] in enumerate(linklist):
    dateg = timestamp.split()[0]
    timeg = timestamp.split()[1]
    if gred[0] == '-':
        greencurrencyv=None
        greenunitsv=None
        redunitsv=gred.split()[0]
        redcurrencyv=gred.split()[1]
    else:
        greencurrencyv=gred.split()[0]
        greenunitsv=gred.split()[1]
        redunitsv=None
        redcurrencyv=None
    othercurv = movr.split()[0]
    otherunitsv = movr.split()[1]
    writeToExcelFile(index+1, dateg, timeg, greencurrencyv, redunitsv, othercurv)


wb.save('cryptoscrapingtwo.xlsx')
