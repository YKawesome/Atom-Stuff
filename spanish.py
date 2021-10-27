import urllib.request, urllib.parse, urllib.error
t
verb='conducir'
form='present'

bru = ssl.create_default_context()
bru.check_hostname = False
bru.verify_mode = ssl.CERT_NONE
verb=verb.lower()
url = "https://www.spanishdict.com/conjugate/" + verb
form=form.lower()
html = urllib.request.urlopen(url, context=bru).read()
soup = BeautifulSoup(html, "html.parser")
#soup is a changeable variable names
#retrieve all anchor tags



x = soup.find_all("table",class_='vtable--2WLTGmgs')[0]
y = x.find_all("tr")

headers=y[0]
yo=y[1]
tu=y[2]
el=y[3]
nosotros=y[4]
vosotros=y[5]
ellos=y[6]




forms = {
"present": 1,
"preterite": 2,
"imperfect": 3,
"conditional": 4,
"future": 5
}

oldform = form
form = forms[form]

yo = yo.find_all('a')[form]['aria-label']
tu= tu.find_all('a')[form]['aria-label']
el= el.find_all('a')[form]['aria-label']
nosotros= nosotros.find_all('a')[form]['aria-label']
vosotros= vosotros.find_all('a')[form]['aria-label']
ellos= ellos.find_all('a')[form]['aria-label']
