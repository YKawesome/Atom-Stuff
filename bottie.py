import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

bru = ssl.create_default_context()
bru.check_hostname = False
bru.verify_mode = ssl.CERT_NONE

# verb = input("Verb: ")

url = "https://www.spanishdict.com/conjugate/" + verb
# form = input("Form: ").lower()
form=form.lower()
html = urllib.request.urlopen(url, context=bru).read()
soup = BeautifulSoup(html, "html.parser")
#soup is a changeable variable names
#retrieve all anchor tags


try:
    x = soup.find_all("div",class_='_2R9Nsmma')[0].find_all('tr')
except:
    #ctx.send(That's not a Spanish Verb!)
    #return

headers=x[0]
yo=x[1]
tu=x[2]
el=x[3]
nosotros=x[4]
vosotros=x[5]
ellos=x[6]

forms = {
"present": 0,
"preterite": 1,
"imperfect": 2,
"conditional": 3,
"future": 4
}

try:
    form = forms[form]
    yo = yo.find_all('a')[form]['aria-label']
    tu= tu.find_all('a')[form]['aria-label']
    el= el.find_all('a')[form]['aria-label']
    nosotros= nosotros.find_all('a')[form]['aria-label']
    vosotros= vosotros.find_all('a')[form]['aria-label']
    ellos= ellos.find_all('a')[form]['aria-label']
except:
    #ctx.send("That's not a valid/registered form!")
    #return



# embed=discord.Embed(title=f"CONJUGATION OF {verb}", description="Preterite Form",color=discord.Color.blue())
# embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple124/v4/d4/00/c0/d400c0f2-9d30-3829-0cf2-9ca1a61dd351/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1024x1024bb.png")
# embed.add_field(name="Yo", value=yo, inline=True)
# embed.add_field(name="Nosotros", value=nosotros, inline=True)
# embed.add_field(name="Tú", value=tu, inline=True)
# embed.add_field(name="Vosotros", value=vosotros, inline=True)
# embed.add_field(name="Él/Ella/Usted", value=el, inline=True)
# embed.add_field(name="Ellos/Ellas/Ustedes", value=ellos, inline=True)
# embed.set_footer(text="Provided by SpanishDict")
# await ctx.send(embed=embed)
