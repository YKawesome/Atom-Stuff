from discord.ext import commands
import json
import discord
import urllib.request, urllib.parse, urllib.error
# from googletrans import Translator
from bs4 import BeautifulSoup
import ssl



with open('json/files.json') as f:
  data = json.load(f)

class SCHOOL(commands.Cog,description='school-related commands'):
  def __init__(self, bot):
    self.bot = bot
  
  def is_in_guild(guild_ids):
    async def predicate(ctx):

      go = False
      for thing in guild_ids:
        if ctx.guild.id == thing:
          go = True
          break

      return ctx.guild and go
    return commands.check(predicate)
    
  # @commands.command(name='translate',help='translate some text',aliases=['tran'])
  # async def translating(self,ctx,query:str):
  #   print(query)
  #   translator = Translator('translate.google.com')
  #   print(translator)
  #   translation = translator.translate('안녕하세요')
    
  #   print(translation)
  #   print(translation.src)
  #   print(translation.dest)
  #   print(translation.text)

  @commands.group(name='calc', help='Calc Commands Header')
  async def calc(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and .help one of them')
  
  @calc.group(name='derivatives',help='Derivative info', aliases=["der"])
  async def derivatives(self,ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and .help one of them')

  @derivatives.command(name='sinx',help='derivative of sinx', aliases=['sin'])
  async def sinx(self,ctx):
    await ctx.send('cos(x)')
  
  @derivatives.command(name='cosx',help='derivative of cosx', aliases=['cos'])
  async def cosx(self,ctx):
    await ctx.send('-sin(x)')
  
  @derivatives.command(name='tanx',help='derivative of tanx', aliases=['tan'])
  async def tanx(self,ctx):
    await ctx.send('-sec^2(x)')
  
  @derivatives.command(name='cotx',help='derivative of cotx', aliases=['cot'])
  async def cotx(self,ctx):
    await ctx.send('-csc^2(x)')
  
  @derivatives.command(name='secx',help='derivative of secx', aliases=['sec'])
  async def secx(self,ctx):
    await ctx.send('sec(x)tan(x)')
  
  @derivatives.command(name='cscx',help='derivative of cscx', aliases=['csc'])
  async def cscx(self,ctx):
    await ctx.send('-csc(x)cot(x)')
  
  @derivatives.command(name='e^x',help='derivative of e^x', aliases=['ex'])
  async def derex(self,ctx):
    await ctx.send('e^x')
  
  @derivatives.command(name='lnx',help='derivative of lnx', aliases=['ln'])
  async def derln(self,ctx):
    await ctx.send('1/x')
  
  @derivatives.command(name='sum',help='derivative of sum')
  async def dersum(self,ctx):
    await ctx.send("d/dx (f(x)+g(x)) = f'(x) + g'(x)")
  
  @derivatives.command(name='product',help='derivative of product')
  async def derproduct(self,ctx):
    await ctx.send("d/dx (f(x)g(x)) = f'(x)g(x) + g'(x)f(x)")
  
  @derivatives.command(name='quotient',help='derivative of quotient')
  async def derquotient(self,ctx):
    await ctx.send("d/dx (f(x)/g(x)) = (f'(x)g(x) - g'(x)f(x))/g(x)^2")
  
  @derivatives.command(name='powerrule',help='derivative of powers', aliases=['powerr'])
  async def powerrule(self,ctx):
    await ctx.send("d/dx (x^n) = nx^(n-1)")
  
  @derivatives.command(name='power',help='differentiate a monomial. Give input in the form ax^n.',aliases=['pow'])
  async def power(self,ctx,expression:str):
    result = expression.split('x')
    exp = result[-1]
    if result[0] == '':
      a = 1
    else:
      a = result[0]

    final = str(float(a)*float(exp[1:])) + 'x^' + str(float(result[-1][1:])-1)
    # final = str(float(exp))
    await ctx.send(final)



  
  


    

    
  @commands.group(name='periodic', help='Gives a periodic table of ions or regular', aliases=["per"])
  async def periodic(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and .help one of them')
  
  @periodic.command(name='table',help='gives periodic table')
  async def table(self,ctx):
    embed=discord.Embed(title="PERIODIC TABLE OF ELEMENTS", description="[Table](https://cdn.discordapp.com/attachments/621213039202402315/829509660448260127/BasicTable.pdf)")
    embed.set_footer(text="Thank you to Mrs. Kissling!")
    await ctx.send(embed=embed)

  # @periodic.command(name='ions',help='gives periodic table (ions)')
  # async def ions(self,ctx):
  #   embed=discord.Embed(title="POLAR GRAPHING PAPER", description="[Graphing Paper](https://cdn.discordapp.com/attachments/621213039202402315/829509645956808714/PT_ions.pdf)")
  #   embed.set_footer(text="Thank you to Mrs. Kissling!")
  #   await ctx.send(embed=embed)


  @commands.command(name='conjugate',help='conjugates a verb by name and form',aliases=['con'])
  async def conjugate(self,ctx,verb:str,form='present'):
    bru = ssl.create_default_context()
    bru.check_hostname = False
    bru.verify_mode = ssl.CERT_NONE
    verb=verb.lower()
    url = "https://www.spanishdict.com/conjugate/" + verb
    form=form.lower()
    html = urllib.request.urlopen(url, context=bru).read()
    soup = BeautifulSoup(html, "html.parser")
    #the above is meant to format the form and verb, and prepare the web extraction



    x = soup.find_all("table",class_='vtable--2WLTGmgs')[0]
    # looking for specific tables and the first one because the webpage has that for the conjugation chart I want
    y = x.find_all("tr")
    # looking for all of the table rows

    # headers=y[0]
    yo=y[1]
    tu=y[2]
    el=y[3]
    nosotros=y[4]
    vosotros=y[5]
    ellos=y[6]
    # all of the pronouns that matter for conjugation



    forms = {
    "present": 0,
    "preterite": 1,
    "imperfect": 2,
    "conditional": 3,
    "future": 4
    }

    # forms placeholder (technically using the actual form would be better but I'm lazy)

    oldform = form
    form = forms[form]

    # preserve the form and use a form integer from the aforementioned forms dictionary (im lazy once again)

    yo = yo.find_all('a')[form]['aria-label']
    tu= tu.find_all('a')[form]['aria-label']
    el= el.find_all('a')[form]['aria-label']
    nosotros= nosotros.find_all('a')[form]['aria-label']
    vosotros= vosotros.find_all('a')[form]['aria-label']
    ellos= ellos.find_all('a')[form]['aria-label']

    # find all of the conjugatins (aria-label happens to have it without additional formatting)
    

    tra = soup.find_all("div",id='quickdef1-es')[0].a.string
    tralist = tra.split()
    finastring = ''
    for item in tralist:
      finastring += item[0].upper() + item[1:] + ' '
    finastring = finastring.strip()

    # unnecessary complication to find definition

    
    try:    
      embed=discord.Embed(title=f"CONJUGATION OF {verb.upper()}", description=f"[{oldform.capitalize()} Form]({url})",color=discord.Color.blue())
      embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple124/v4/d4/00/c0/d400c0f2-9d30-3829-0cf2-9ca1a61dd351/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1024x1024bb.png")
      embed.add_field(name="Translation",value=finastring,inline=False)
      embed.add_field(name="Yo", value=yo, inline=True)
      embed.add_field(name="Nosotros", value=nosotros, inline=True)
      embed.add_field(name="Tú", value=tu, inline=True)
      embed.add_field(name="Vosotros", value=vosotros, inline=True)
      embed.add_field(name="Él/Ella/Usted", value=el, inline=True)
      embed.add_field(name="Ellos/Ellas/Ustedes", value=ellos, inline=True)
      embed.set_footer(text="Provided by SpanishDict, coded by Yoo sef :D")
      await ctx.send(embed=embed)
      # send it all
    except:
        await ctx.send("That's not a valid/registered form!")
        return


  @commands.command(name='polar',help='gives polar paper')
  async def polar(self,ctx):
    embed=discord.Embed(title="POLAR GRAPHING PAPER", description="[Graphing Paper](https://cdn.discordapp.com/attachments/768251357341417482/809302654919770142/Polar_Graph_Paper.pdf)")
    embed.set_footer(text="Thank you to Hari!")
    await ctx.send(embed=embed)
    

  @commands.group(name='whap', help='Finds the WHAP text for the chapter you query; THESE FILES ARE SEARCHABLE WITH COMMAND F OR CTRL F BECAUSE AN OCR WAS RUN ON THEM', aliases=["wh"])
  async def whap(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and *help popquote one of them')
  
  @whap.command(name='amsco', help='Search AMSCO', aliases=['am'])
  async def amsco(self, ctx, chapter: int):
    try:
      d = "[Chapter " + str(chapter) + "](" + data["amsco"][str(chapter)] + ")"
      embedVar = discord.Embed(title="AMSCO", description=d, color=0x00ff00)
      await ctx.send(embed=embedVar)
    except:
      await ctx.send("You may not have entered a valid chapter. Make sure to enter parameters in the right order. Maybe you typed something wrong. Please check *help for more information on this command, or dm the Yoo sef for help.")

  @whap.command(name='teaip', help='Search teaip', aliases=['te'])
  async def teaip(self, ctx, chapter: str):
    try:
      d = "[Chapter " + str(chapter) + "](" + data["teaip"][str(chapter)] + ")"
      embedVar = discord.Embed(title="TEAIP", description=d, color=0x00ff00)
      await ctx.send(embed=embedVar)
    except:
      await ctx.send("You may not have entered a valid chapter. Make sure to enter parameters in the right order. Maybe you typed something wrong. Please check *help for more information on this command, or dm the Yoo sef for help.")
  
  @commands.command(name='apush', help='Finds the APUSH text for the chapter you query; THIS IS THE 14TH EDITION, NOT THE MOST RECENT.', aliases=["us"])
  async def apush(self, ctx, chapter: int):
    try:
      d = "[Chapter " + str(chapter) + "](" + data["apush"][str(chapter)] + ")"
      embedVar = discord.Embed(title="AMERICAN PAGEANT", description=d, color=0x00ff00)
      await ctx.send(embed=embedVar)
    except:
      await ctx.send("You may not have entered a valid chapter. Make sure to enter parameters in the right order. Maybe you typed something wrong. Please check *help for more information on this command, or dm the Yoo sef for help.")
    

  @commands.command(name='englishgrade',help='Calculate your english grade given your other grades',aliases=['engrade'])
  async def engrade(self,ctx):
    def check(author):
        def inner_check(message):
          # if not message.content.lower() == None:
          return message.author == author and (True)
        return inner_check
    
    await ctx.send('What is your current grade in the class?')
    msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
    currgrade=msg.content
    
      

  # @commands.command(name='goodreads',help='queries goodreads for a book and returns the title and link',aliases=['gr'])
  # @commands.cooldown(1, 30, commands.BucketType.user)
  # async def goodreads(self,ctx,*,title: str):
  #   bru = ssl.create_default_context()
  #   bru.check_hostname = False
  #   bru.verify_mode = ssl.CERT_NONE
  #   lol = ''
  #   for pop in title.split():
  #     lol+=pop+'%20'
  #   lol = lol.strip()

    
  #   url = "https://www.goodreads.com/search?query=" + lol

  #   html = urllib.request.urlopen(url, context=bru).read()

  #   soup = BeautifulSoup(html, "html.parser")

  #   x = soup.find_all("tr", itemtype="http://schema.org/Book")[0].find_all('a')[0]


  #   link = "https://www.goodreads.com" + x.get('href')
  #   fintitle = x.get('title')
  #   d = f"[{fintitle}]({link})"
  #   embedVar = discord.Embed(title="GOODREADS QUERY", description=d, color=0x197419)

  #   html = urllib.request.urlopen(link, context=bru).read()
  #   soup = BeautifulSoup(html, "html.parser")

  #   x = soup.find_all("img", id="coverImage")[0]
  #   lolm = x.get('src')
  #   embedVar.set_image(url=lolm)
  #   await ctx.send(embed=embedVar)

def setup(bot: commands.Bot):
    bot.add_cog(SCHOOL(bot))






