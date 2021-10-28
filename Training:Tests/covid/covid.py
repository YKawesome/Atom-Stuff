import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

bru = ssl.create_default_context()
bru.check_hostname = False
bru.verify_mode = ssl.CERT_NONE

url = "https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html"
html = urllib.request.urlopen(url, context=bru).read()
soup = BeautifulSoup(html, "html.parser")
#soup is a changeable variable names
#retrieve all anchor tags


state = input('State or territory: ').lower()
state=state.lower()
listnames=[]
listre=[]
x = soup.find_all("tr", class_="g-row g-body-row g-region")
z=0
for y in x:
    if z >= 61:
        break
    listre.append(y)

    z+=1

for thing in listre:
    listnames.append(thing.find_all('span')[0].find_all('span')[0].string.lower())

print(listnames)



# print(type(thing))
ind=listnames.index(state)

ye = listre[ind]

new = ye.find_all('p')

oneshot=new[0]
twoshot=new[1]
dosdel=new[2]
shotsgiven=new[3]
dosused=new[4]
