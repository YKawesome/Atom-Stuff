
from discord.ext import commands
import json
import discord
import urllib.request, urllib.parse, urllib.error


from bs4 import BeautifulSoup
import ssl


class INFO(commands.Cog,description='informational commands'):
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



  @commands.command(name='prefix',help='Displays the prefixes for the bots in Beckman Sophomores')
  @is_in_guild([612845460360527883])
  async def prefixes(self,ctx):
    embed=discord.Embed(title="PREFIXES", description="Prefixes used in Beckman Sophomores", color=0xffffff)
    embed.add_field(name="Dyno", value="Prefix: ?", inline=True)
    embed.add_field(name="Rythm", value="Prefix: !", inline=True)
    embed.add_field(name="Rythm 2", value="Prefix: >", inline=True)
    embed.add_field(name="Groovy", value="Prefix: -", inline=True)
    embed.add_field(name="Botify", value="Prefix: $botify", inline=True)
    embed.add_field(name="Poll Bot", value="Prefix: +", inline=True)
    embed.add_field(name="Mudae", value="Prefix: $", inline=True)
    embed.add_field(name="Chess", value="Prefix: |", inline=True)
    embed.add_field(name="Dank Memer", value="Prefix: pls", inline=True)
    embed.add_field(name="MathBot", value="Prefix: =", inline=True)
    embed.add_field(name="Yggdrasil", value="Prefix: --", inline=True)
    embed.add_field(name="Counting", value="Prefix: c!", inline=True)
    embed.add_field(name="Reaction Roles", value="Prefix: rr!", inline=True)
    embed.add_field(name="DIY (Me)", value="Prefix: *", inline=True)
    embed.set_footer(text="Built by The Architect, Yoo sef :D")
    await ctx.send(embed=embed)

  #0097CF
  @commands.group(name='link',help='Embed a Hyperlink. Paste the link first, then a title (can be multiple words)')
  async def link(self,ctx,link:str,*,title:str):
    footer = f'Sent by {str(ctx.author)}'
    title=title.upper()
    embed=discord.Embed(title=title, url=link, color=0x0097cf)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    lmsg = await ctx.fetch_message(ctx.message.id)
    await lmsg.delete()

  @commands.group(name='opt',help='optin/optout')
  async def opt(self,ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Look at the subcommands list, random, and write and *help opt one of them')
  @opt.command(name='out',help='opt out of the "im" autoresponder')
  async def out(self,ctx):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name="optout")
    await discord.Member.add_roles(member, role)
    await ctx.send('Successfully opted out.')
  @opt.command(name='in',help='opt into of the "im" autoresponder')
  async def into(self,ctx):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name="optout")
    await discord.Member.remove_roles(member, role)
    await ctx.send('Successfully opted in.')

  @commands.command(name='vaccine',help='gets vaccine stats for a state or territory; if you want the us total, dont type anything after vaccine',aliases=['vac','cure'])
  async def vaccine(self,ctx,*,state=None):
    bru = ssl.create_default_context()
    bru.check_hostname = False
    bru.verify_mode = ssl.CERT_NONE

    url = "https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html"
    html = urllib.request.urlopen(url, context=bru).read()
    soup = BeautifulSoup(html, "html.parser")
    #soup is a changeable variable names
    #retrieve all anchor tags

    sendit = False
    # state = input('State or territory: ').lower()
    if not state==None:
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




    # print(type(thing))
    try:
      ind=listnames.index(state)
      sendit = True
    except:
      sendit = False
      if state == None:
        sendit=True
        ind=0
    
    if sendit:
      ye = listre[ind]
      new = ye.find_all('p')

      oneshot=new[0].string
      twoshot=new[1].string
      dosdel=new[2].string
      shotsgiven=new[3].string
      dosused=new[4].string

      if ind == 0:
        embedVar = discord.Embed(title="VACCINE ROLLOUT IN US", description=f"Credit: [New York Times]({url})", color=0x24a8be)
      else:
        embedVar = discord.Embed(title="VACCINE ROLLOUT IN " + state.upper(), description=f"Credit: [New York Times]({url})", color=0x24a8be)
      embedVar.add_field(name="Percent With At Least One Shot", value=oneshot, inline=False)
      embedVar.add_field(name="Percent With Two Shots", value=twoshot, inline=False)
      embedVar.add_field(name="Doses Delivered", value=dosdel, inline=False)
      embedVar.add_field(name="Shots Given", value=shotsgiven, inline=False)
      embedVar.add_field(name="Percent of Doses Used", value=dosused, inline=False)
      embedVar.set_thumbnail(url='https://www.vippng.com/png/detail/170-1704302_graphic-library-stock-pill-clipart-syringe-transparent-vaccine.png')
      await ctx.send(embed=embedVar)
    else:
      await ctx.send("Invalid State/Territory")

  @commands.command(name='states',help='gets states and territories compatible with the vaccine command')
  async def states(self,ctx):
    await ctx.send(['u.s. total*', 'american samoa', 'palau', 'northern mariana islands', 'alaska', 'guam', 'west virginia', 'new mexico', 'connecticut', 'north dakota', 'oklahoma', 'washington, d.c.', 'south dakota', 'virginia', 'delaware', 'wisconsin', 'arkansas', 'maine', 'vermont', 'hawaii', 'wyoming', 'oregon', 'montana', 'kentucky', 'minnesota', 'north carolina', 'washington', 'louisiana', 'michigan', 'california', 'colorado', 'new jersey', 'florida', 'arizona', 'mississippi', 'utah', 'new york', 'massachusetts', 'indiana', 'new hampshire', 'nevada', 'south carolina', 'ohio', 'georgia', 'illinois', 'maryland', 'texas', 'pennsylvania', 'nebraska', 'tennessee', 'idaho', 'rhode island', 'kansas', 'missouri', 'alabama', 'marshall islands', 'iowa', 'puerto rico', 'u.s. virgin islands', 'micronesia', 'federal agencies'])

def setup(bot: commands.Bot):
    bot.add_cog(INFO(bot))






