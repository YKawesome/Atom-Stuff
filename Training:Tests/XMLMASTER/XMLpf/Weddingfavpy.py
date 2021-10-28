import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum = sum + int(count.text)
print(sum)
