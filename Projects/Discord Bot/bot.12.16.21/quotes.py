from discord.ext import commands
import json
import discord
import random

import os,glob

y=False

with open('json/popquotes/Hamilton_Quotes.json') as thingie:
  quotes = json.load(thingie)

with open('json/popquotes/officequotes.json') as yetanother:
  office_quotes = json.load(yetanother)

with open('json/popquotes/jojo.json') as jojostuff:
  jojotxt = json.load(jojostuff)

class QUOTES(commands.Cog,description='Anything to do with quotes'):
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

  @commands.group(name='popquote',help='Picks a random quote from a show specified',aliases=['pq'])
  async def popquote(self,ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and *help popquote one of them')

  @popquote.command(name='hamilton',help='Sends a random hamilton quote | Credit: Audrey Su for compiling the list',aliases=['ham'])
  async def hamilton(self, ctx):
    achoice = random.choice(quotes)
    await ctx.send(achoice)

  @popquote.command(name='office',help='Responds with a random quote from the Office')
  async def office(self, ctx):
    response = random.choice(office_quotes)
    await ctx.send(response)

  @popquote.command(name='jojo',help='Responds with a random quote from Jojo | Credit: Dhruv for making the list')
  @commands.has_any_role('weebs','adminrole')
  async def jojo(self,ctx):
    await ctx.send(random.choice(jojotxt))

  @commands.group(name='quote',help='the quoting feature',aliases=['q'])
  @is_in_guild([612845460360527883])
  async def quote(self,ctx):
      if ctx.invoked_subcommand is None:
        await ctx.send('Look at the subcommands list, random, and write and *help quote one of them')

  @quote.command(name='write',help='writes to a quote file',aliases=['w'])
  @commands.has_permissions(administrator=True)
  async def write(self, ctx, name: str, *, quote: str):
    def check(author):
      def inner_check(message):
        if message.content.lower()=='y':
          global y
          y=True
        return message.author == author and (message.content.lower() == "y" or message.content.lower() == "n")
      return inner_check
    await ctx.send(f'Are you sure you would like to save the quote "{quote}" to user {name}? y/n')
    msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
    global y
    if msg and y:
      y=False
      try:
        with open('json/quotes/' + name + '.txt','a') as the_file1:
          the_file1.write(quote + '\n')
        await ctx.send('"'+quote+'" saved to the '+name+' quote file')
      except:
        await ctx.send("That user isn't registered.")
    else:
      await ctx.send("Cancelled.")
  
  
  @quote.command(name='random',help='sends a random quote from someone specified. Type *quote random name for a quote from someone or *quote random all (or just don\'t specify a person) for a random quote from the whole library.',aliases=['r'])
  async def rando(self,ctx,name='all'):
    listy=[]
    if not name.lower()=='all':
      yfile= open(f'json/quotes/{name.lower()}.txt', 'r')
      for x in yfile:
        listy.append(x)
  
    elif name.lower()=='all':
      folder_path = 'json/quotes'
      for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        
        if not filename == 'json/quotes/walter.txt':
          with open(filename, 'r') as f:
            for poo in f:
              listy.append(poo)

    else:
      listy.append("Invalid name")

    response = random.choice(listy)
    await ctx.send('"'+response.strip('\n')+'"')

  @quote.command(name='list',help='list of people registered with this',aliases=['l'])
  async def qlist(self,ctx):
    folder_path = 'json/quotes'
    done=''
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
      done+=filename[12:].split('.txt')[0] + ', '
    done=done[:-2]
    embed=discord.Embed(title="Quote Members", description=done,color=0x00fffb)
    await ctx.send(embed=embed)
      


  @quote.command(name='game',help='Guess who said it!',aliases=['g'])
  async def qgame(self,ctx):
    folder_path = 'json/quotes'
    listy=[]
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
      if not filename == 'json/quotes/walter.txt':
        with open(filename, 'r') as f:
          for poo in f:
            listy.append(poo)
    
    response = random.choice(listy)
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
      with open(filename, 'r') as f:
        if response in f:
          response = (response.strip(),filename.split('/')[2][:-4])
    

    def check(author):
        def inner_check(message):
          if not message.content.lower() == None:
            global y
            y=True
          return message.author == author and (True)
        return inner_check

    embed=discord.Embed(color=0x00fffb)
    embed.add_field(name="Who said it?", value=response[0], inline=True)
    embed.set_footer(text="Try *q l for a list of people you can use as answers!")
    await ctx.send(embed=embed)

    msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
    global y
    if msg and y:
      y=False
      if msg.content.lower() == response[1]:
        embed=discord.Embed(color=0x1eff00)
        embed.add_field(name="CORRECT", value=f"You got it! It was {response[1]}!", inline=True)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name="INCORRECT", value=f"You were wrong :/ It was {response[1]}.", inline=True)
        await ctx.send(embed=embed)


  
  @quote.command(name='newfile',help='adds a new file',aliases=['nf'])
  @commands.has_permissions(administrator=True)
  async def newfile(self,ctx,name:str):
    def check(author):
      def inner_check(message):
        if message.content.lower()=='y':
          global y
          y=True
        return message.author == author and (message.content.lower() == "y" or message.content.lower() == "n")
      return inner_check
    await ctx.send(f'Are you sure you would like create the file {name}.txt? y/n')
    msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
    global y
    if msg and y:
      y=False
      f= open(f"json/quotes/{name}.txt","w+")
      await ctx.send(f'{name}.txt was created.')
    

  @commands.group(name='copypasta',help='the copypasta group',aliases=['cp'])
  async def copypasta(self,ctx):
    if ctx.invoked_subcommand == None:
      ctx.send("Look at the subcommands for this one")
  
  @copypasta.command(name='add',help='Add a copypasta')
  @commands.has_permissions(administrator=True)
  async def addit(self,ctx,trigger:str,*,response:str):
    def check(author):
      def inner_check(message):
        if message.content.lower()=='y':
          global y
          y=True
        return message.author == author and (message.content.lower() == "y" or message.content.lower() == "n")
      return inner_check
    await ctx.send(f'Are you sure you would like to add the response {response} to trigger {trigger}? y/n')
    msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
    global y
    if msg and y:
      y=False
      try:
        with open('json/copypasta.txt','a') as the_file:
          the_file.write(f'{trigger}:{response}' + '\n')
        await ctx.send("Added.")
      except:
        await ctx.send("That user isn't registered.")
    else:
      await ctx.send("Cancelled.")
  
  @copypasta.command(name='list',help="returns a list of the copypastas")
  async def listofthem(self,ctx):
    listy=[]
    thefile= open('json/copypasta.txt', 'r')
    for x in thefile:
      listy.append(x.split(':')[0])
    await ctx.send(listy)

def setup(bot: commands.Bot):
    bot.add_cog(QUOTES(bot))






