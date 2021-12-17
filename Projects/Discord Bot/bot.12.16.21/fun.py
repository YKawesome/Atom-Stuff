import random
import requests
import discord
from discord.ext import commands
import json
from discord.utils import get

with open('json/riddles.json') as lol:
  data = json.load(lol)
with open('json/animals.json') as rofl:
  yaylist = json.load(rofl)
with open('json/emojis.json') as emjs:
  emjies = json.load(emjs)
snipe=''

class FUN(commands.Cog,description="Miscellaneous/fun commands suggested by members"):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_message_delete(self,ctx):
    if not ctx.author.bot:
      global snipe
      snipe=ctx

  @commands.command(name='snipe',help='snipes the last message')
  async def snipe(self,ctx):
    if ctx.channel == snipe.channel:
      embed=discord.Embed(description=snipe.content)
      embed.set_author(name=snipe.author, icon_url=snipe.author.avatar_url)
      dateish=snipe.created_at
      embed.set_footer(text=str(dateish.month)+'/'+str(dateish.day-1)+'/'+str(dateish.year))
      await ctx.send(embed=embed)
    else:
      lmsg = await ctx.fetch_message(ctx.message.id)
      await lmsg.delete()

  @commands.command(name='react',help='reacts')
  async def react(self,ctx,word:str,lmsg:discord.Message):
    def isUniqueChars(thing):
 
      # String length cannot be more than
      # 256.
      if len(thing) > 256:
          return False
  
      # Initialize occurrences of all characters
      char_set = [False] * 128
  
      # For every character, check if it exists
      # in char_set
      for i in range(0, len(thing)):
  
          # Find ASCII value and check if it
          # exists in set.
          val = ord(thing[i])
          if char_set[val]:
              return False
  
          char_set[val] = True
  
      return True
    def split(word):
      return [char for char in word]
    
    if isUniqueChars(word):
      for char in split(word):
        await lmsg.add_reaction(emjies[char.upper()])
    else:
      await ctx.send('Please choose a word with unique characters.')

  # @commands.command(name='color',help='changes the color of a role')
  # async def colorchange(self,ctx,hexcode:discord.Color,*,role:discord.Role):
  #   changeableroles = ['Server Booster','adminrole','Server Booster (Legacy)','PEASANTS','prime minister']
  #   member = ctx.author

  #   if not member.guild_permissions.administrator:
  #     if str(role) in changeableroles and get(member.roles, name=str(role)):
  #       await role.edit(colour=hexcode)
  #       await ctx.send(f'Changed role "{str(role)}" color to {str(hexcode)}')
  #     else:
  #       await ctx.send("That role doesn't exist, you can't change that role, or you don't have it.")
  #   else:
  #     if get(member.roles, name=str(role)):
  #       await role.edit(colour=hexcode)
  #       await ctx.send(f'Changed role "{str(role)}" color to {str(hexcode)}')
  #     else:
  #       await ctx.send("That role doesn't exist, you can't change that role, or you don't have it.")
  
  @commands.command(name='teachme',help='teach me ____ teach me ___',aliases=['tm'])
  async def teach(self,ctx,*,thing:str):
    await ctx.send(f'teach me {thing.upper()} teach me teach me {thing.upper()}')


  @commands.command(name='animal',help='Sends a random animal with the specified letter at the beginning | Credit: Hari for the idea',aliases=['an'])
  async def animal(self,ctx,letter=None):
    sublist = []
    if not letter==None:
      try:
        for link,element in yaylist:
          if element[0].lower() == letter:
            sublist.append([link,element])
        #[here](your_link_goes_here)
        almostresponse = random.choice(sublist)
        wee = '[' + almostresponse[1] + '](' + almostresponse[0] + ')'
        embedVar = discord.Embed(title="ANIMAL", description=wee, color=0xf6f658)
        await ctx.send(embed=embedVar)
      except:
        response = 'Invalid character'
    else:
      almostresponse = random.choice(yaylist)
      wee = '[' + almostresponse[1] + '](' + almostresponse[0] + ')'
      embedVar = discord.Embed(title="ANIMAL", description=wee, color=0xf6f658)
      await ctx.send(embed=embedVar)
    await ctx.send(response)

  

  @commands.command(name='reverse',help='reverses your nickname',aliases=['rev'])
  async def reverse(self,ctx):
    if not ctx.author.nick  == None:
      await ctx.send(ctx.author.nick[::-1])
    else:
      ans = str(ctx.author)
      response = ans.split('#')[0]
      await ctx.send(response[::-1])

  
  @commands.command(name='pickupline',help='Sends a pick up line, multi-word subjects allowed | credits to Ian and Brian for construction/writing', aliases=['pl'])
  async def pickup(self,ctx, *, victim = None):
    with open('json/pickuplines.json') as anotherone:
      biglist = json.load(anotherone)
    choice = random.choice(biglist)
    if victim == None:
      await ctx.send(choice)
    else:
      choice = choice[:-1] + " " + str(victim) + choice[-1]
      await ctx.send(choice)
  
  @commands.command(name='plcovid',help='covid variant',aliases=['plc'])
  async def covid(self,ctx,*,victim=None):
    listy = []
    thefile= open('json/covid.txt', 'r')
    for x in thefile:
      listy.append(x)
    choice = random.choice(listy)
    if victim == None:
      await ctx.send(choice)
    else:
      uh = choice.strip()[:-1] + " " + str(victim) + choice.strip()[-1]
      await ctx.send(uh)

  @commands.command(name='riddle',help='Sends a random riddle with spoiler tagged answer',aliases=['rd'])
  async def riddle(self,ctx,rid='insert'):
    rid = random.randint(0,98)
    await ctx.send(data[rid]['question'] + " Answer: ||" + data[rid]['answer'] + "||")

  @commands.command(name='ping',help='Gives latency of the pong') 
  async def ping(self, ctx):
    await ctx.send("Pong! `" + str(int(round(self.bot.latency,4)*1000)) + " ms`")
    # str(float('{0}'.format(round(self.bot.latency, 2))*1000)))


  

  @commands.command(name='rolldice', help='Simulates rolling dice.',aliases=['dice','roll'])
  async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    total = 0
    for thing in dice:
      total+=int(thing)
    # print(dice)
    embed=discord.Embed(title="Dice Roll", description=f'Rolled {str(number_of_dice)} dice with {str(number_of_sides)} sides each',color=0x009dff)
    for index,item in enumerate(dice):
      embed.add_field(name=f"Dice {str(index)}", value=str(item), inline=True)
    embed.add_field(name='Total', value=str(total), inline=False)
    await ctx.send(embed=embed)

  
  @commands.command(name='yt', help='Queries youtube for a youtuber and returns the channel, please do not overuse this as I only get 100 requests a day')
  @commands.cooldown(1, 300, commands.BucketType.default)
  async def search(self, ctx, *, query: str):
    query.replace(" ", "+")

    headers = {
        'key': "AIzaSyCt-wqfhbdhhkyBION8YP-lr3ZU6-9_HNQ",
        'apilink': "https://www.googleapis.com/customsearch/v1",
        'cx': "1ffb260c3faceaacd",
        'cr': "countryUS",
        'lr': "lang_en"
        }

    response = requests.get(headers['apilink'] + "?key=" + headers['key'] + "&c2coff=1" + "&cr=" + headers['cr'] + "&cx=" + headers['cx'] + "&lr" + headers['lr'] + "&num=3" + "&q=" + query)

    data = response.json()

    final = data["items"][0]["link"]
    # finaldos = 
    await ctx.send(final)


def setup(bot: commands.Bot):
    bot.add_cog(FUN(bot))