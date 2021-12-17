# @bot.command(name='zoom',help='Gives the zoom link for a certain class')
# async def zoom(ctx, teacher: str, period: int):
#     if teacher in data:
#       if ((period<len(data[teacher])) and (period>=0)):
        
#         if data[teacher][period] != "p":
#           response = data[teacher][period]
#         else:
#           response = "That period hasn't been logged yet. Please wait and we will try to implement it."
#       else:
#         response = "That period hasn't been logged yet. Please wait and we will try to implement it."
#     else:
#       response = "That teacher hasn't been logged yet. Please wait and we will try to implement it."
#     await ctx.send(response)

  # @quote.command(name='list',help='sends a list of quotes of yousef, ian, or jeff')
  # async def listit(self, ctx, name:str):
  #   if name.lower()=='yousef':
  #     yfile= open('json/quotes/yousef.txt', 'r')
  #     i=0
  #     for x in yfile:
  #       if i>=5:
  #         break
  #       i+=1
  #       await ctx.send('"'+x.strip('\n')+'"')
  #   elif name.lower()=='ian':
  #     yfile= open('json/quotes/ian.txt', 'r')
  #     i=0
  #     for x in yfile:
  #       if i>=5:
  #         break
  #       i+=1
  #       await ctx.send('"'+x.strip('\n')+'"')
  #   elif name.lower()=='jeff':
  #     yfile= open('json/quotes/jeff.txt', 'r')
  #     i=0
  #     for x in yfile:
  #       if i>=5:
  #         break
  #       i+=1
  #       await ctx.send('"'+x.strip('\n')+'"')
  #   else:
  #     await ctx.send("Invalid name")

          # if name.lower()=='yousef':
        #   with open('json/quotes/yousef.txt', 'a') as the_file1:
        #     the_file1.write(quote + '\n')
        #   await ctx.send('"'+quote+'" saved to the yousef quote file')
        # elif name.lower()=='ian':
        #   with open('json/quotes/ian.txt', 'a') as the_file2:
        #     the_file2.write(quote + '\n')
        #   await ctx.send('"'+quote+'" saved to the ian quote file')
        # elif name.lower()=='jeff':
        #   with open('json/quotes/jeff.txt', 'a') as the_file3:
        #     the_file3.write(quote + '\n')
        #   await ctx.send('"'+quote+'" saved to the jeff quote file')
        # else:
        #   await ctx.send("That user isn't registered.")

        # @commands.command(name='temp')
  # async def temp(self, ctx):
  #   embed=discord.Embed(title="ERA 3 ESSENTIAL QUESTIONS CHAPTERS", url="https://app.luminpdf.com/viewer/604b81069e28a30012843e28", description="Guide to which chapters to use for different questions\nGet the chapters [here](https://drive.google.com/file/d/1pAof5M3YWMMaO49wG3bBFG5IeEtYyfs6/view?usp=sharing)", color=0x00ccff)
  #   embed.set_author(name="AP WORLD HISTORY- GOLDENBERG", icon_url="https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-0/cp0/p64x64/23467404_10154761234176184_2555660729893564876_o.png?_nc_cat=1&ccb=1-3&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=8XL-y-8XDqwAX9e7E7c&tn=AQ1ol_UO4cKTGXe_&_nc_ht=scontent-lax3-1.xx&_nc_tp=30&oh=6e25812b819249fc857adb3407fe1aac&oe=6081F947")
  #   embed.set_thumbnail(url="https://play-lh.googleusercontent.com/IBKRAvaVCGBFq-hBp6lXlViD4x5lxJXavvSPucMs3vRPSvRQftXCHxdbeHKi5WsqXZ0v")
  #   embed.add_field(name="Chapter 23", value="1-10, 19, 43-45,\n48-52", inline=True)
  #   embed.add_field(name="Chapter 24", value="11-12, 14, 44,\n52", inline=True)
  #   embed.add_field(name="Chapter 25", value="46-49", inline=True)
  #   embed.add_field(name="Chapter 26", value="13, 15-17, 19, 46", inline=True)
  #   embed.add_field(name="Chapter 27", value="22-42, 45", inline=True)
  #   embed.add_field(name="Other", value="18, 20-21, 45", inline=True)
  #   embed.set_footer(text="- Made by Yoo sef :D (the guide is fully complete)")
  #   await ctx.send(embed=embed)

  # def is_in_guild(guild_ids):
  #   async def predicate(ctx):

  #     go = False
  #     for thing in guild_ids:
  #       if ctx.guild.id == thing:
  #         go = True
  #         break

  #     return ctx.guild and go
  #   return commands.check(predicate)