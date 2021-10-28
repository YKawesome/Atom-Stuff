import urllib.request
from bs4 import BeautifulSoup
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
html = opener.open('https://manofmany.com/lifestyle/sex-dating/37-hilarious-covid-19-pick-up-lines')
soup = BeautifulSoup(html, "html.parser")

mydivs = soup.findAll("li")
listy = []
counter = 0
for div in mydivs:
    # listy.append([div.a['href'],div.a.string])
    counter +=1
    if counter>69 and counter<106:
        print(div.string)
# stringie = ''
# for item in listy:
#     stringie+='"'+item+'", '


# for link,element in listy:
    # stringie+='["'+link+'", "'+element+'"], '
# print(stringie)
