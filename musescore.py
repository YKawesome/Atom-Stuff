import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

bru = ssl.create_default_context()
bru.check_hostname = False
bru.verify_mode = ssl.CERT_NONE
z = input("Query: ")
url = "https://musescore.com/sheetmusic?text="+z
html = urllib.request.urlopen(url, context=bru).read()
soup = BeautifulSoup(html, "html.parser")
#soup is a changeable variable names
#retrieve all anchor tags


# x = soup.find_all("a")

print(soup.prettify())

# for y in x:
#     print(y.prettify())
