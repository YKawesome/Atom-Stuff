
import discord
from discord.ext import commands
import random
from discord.utils import get
import asyncio


data = {
  "Beckman Sophomores": "Admin Role",
  "612845460360527883": "⁣        ^ Administrator ^",
  "MC Pipi": "Admin Role",
  "788461886420680815": "Admin",
  "Epic Gamers": "Admin Role",
  "759122338612248598": "admin"

}




listy = []
for key in data:
  listy.append(data[key])

class MODERATION(commands.Cog,description="Moderation commands for admins"):
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
  

  @commands.command(name='temp',help='sends the current embed')
  @commands.has_permissions(administrator=True)
  @is_in_guild([612845460360527883])
  async def temp(self,ctx):
    embed=discord.Embed(title="Less Vs. Fewer", url="https://www.quickanddirtytips.com/education/grammar/less-versus-fewer", description="A guide on when to use each", color=0x2effd5)
    embed.add_field(name="Traditional Rule", value='"Fewer": Countable, "Less": Uncountable"', inline=False)
    embed.add_field(name="Issue/Exception", value="Time, Money, Distance, Weight", inline=False)
    embed.add_field(name="Example 1", value='"We had less than $1000 in the bank."', inline=True)
    embed.add_field(name="Example 2", value='"We\'re Less than 50 miles away."', inline=True)
    embed.add_field(name="Rule That Fixes This", value='Use "less" for singular nouns and "fewer" for plural nouns.', inline=False)
    embed.add_field(name="Example 1", value="Less Candy", inline=True)
    embed.add_field(name="Example 2", value="Less Water", inline=True)
    embed.add_field(name="Example 3", value="Less Potato Salad", inline=True)
    embed.add_field(name="Example 4", value="Fewer M&Ms", inline=True)
    embed.add_field(name="Example 5", value="Fewer Glasses of Water", inline=True)
    embed.add_field(name="Example 6", value="Fewer Potatoes", inline=True)
    embed.add_field(name="Additional Pro", value="Fixes Examples 1 and 2", inline=False)
    embed.add_field(name="Also Fixes", value='"I can fix the roof in less than 12 hours."', inline=False)
    embed.add_field(name="Also Fixes", value='"One less banana" since it is single, but countable.', inline=False)
    embed.add_field(name="Summary", value='Use "Fewer" for Plural and "Less" for Singular', inline=False)
    embed.add_field(name="Link At Top", value="Click for article explaining this rule", inline=True)
    embed.set_footer(text="Created by Yousef Khan :D")
    await ctx.send(embed=embed)

  @commands.command(name='archive',help='Send someone to purgatory',aliases=['arc'])
  @commands.has_permissions(administrator=True)
  @is_in_guild([612845460360527883])
  async def archive(self,ctx, member:discord.Member):
    addrole = discord.utils.get(member.guild.roles, name="ARCHIVE ACCESS")
    await discord.Member.add_roles(member, addrole)
    embed=discord.Embed(title=f":white_check_mark: *{member.name+'#'+member.discriminator} was given archive access*", color=0x00ffaa)
    await ctx.send(embed=embed)

  @commands.command(name='purge',help='Send someone to purgatory')
  @commands.has_permissions(administrator=True)
  @is_in_guild([612845460360527883])
  async def purge(self,ctx, member:discord.Member, amt=None):
    addrole = discord.utils.get(member.guild.roles, name="purgatory")
    remrole = discord.utils.get(member.guild.roles, name="PEASANTS")

    await discord.Member.add_roles(member, addrole)

    try:
      await discord.Member.remove_roles(member, remrole)
    except:
      await ctx.send('That user cannot be sent to purgatory!')
    await ctx.send(f'<@{member.id}> has been **PURGED**.')
    if amt != None:
      try:
        unit=amt[-1]
        amount=int(amt[:-1])
        un=None
        if unit=='s':
          un=1
        elif unit=='m':
          un=60
        elif unit=='h':
          un=3600
        elif unit=='d':
          un=86400
        tot = un*amount
        await asyncio.sleep(tot)

        addrole = discord.utils.get(member.guild.roles, name="PEASANTS")
        remrole = discord.utils.get(member.guild.roles, name="purgatory")

        await discord.Member.add_roles(member, addrole)
        
        try:
          await discord.Member.remove_roles(member, remrole)
        except:
          await ctx.send(f'error: {member} was not revived')
        await ctx.send(f'<@{member.id}> has been **REVIVED**.')
      except:
        await ctx.send('Invalid amount of time!')

  @commands.command(name='revive',help='Send someone to purgatory')
  @commands.has_permissions(administrator=True)
  @is_in_guild([612845460360527883])
  async def revive(self,ctx, member:discord.Member):
    addrole = discord.utils.get(member.guild.roles, name="PEASANTS")
    remrole = discord.utils.get(member.guild.roles, name="purgatory")

    await discord.Member.add_roles(member, addrole)

    try:
      await discord.Member.remove_roles(member, remrole)
    except:
      await ctx.send('That user isn\'t in purgatory!')
    await ctx.send(f'<@{member.id}> has been **REVIVED**.')


  @commands.command(name='mute',help='Stop someone from sending messages')
  @commands.has_permissions(administrator=True)
  async def mute(self,ctx, member:discord.Member, amt=None):
    addrole = discord.utils.get(member.guild.roles, name="Muted")
    try:
      await discord.Member.add_roles(member, addrole)
      embed=discord.Embed(title=f"*{member.name+'#'+member.discriminator} was muted*", color=0x00ffaa)
      await ctx.send(embed=embed)

      if amt != None:
        try:
          unit=amt[-1]
          amount=int(amt[:-1])
          un=None
          if unit=='s':
            un=1
          elif unit=='m':
            un=60
          elif unit=='h':
            un=3600
          elif unit=='d':
            un=86400
          tot = un*amount
          await asyncio.sleep(tot)

          remrole = discord.utils.get(member.guild.roles, name="muted")
          try:
            await discord.Member.remove_roles(member, remrole)
          except:
            await ctx.send(f'error: {member} was not unmuted')
        except:
          await ctx.send('Invalid amount of time!')
    except:
      embed=discord.Embed()
      embed.add_field(name=f":x: I can't find/mute user <@{member.id}>", inline=False)
      await ctx.send(embed=embed)

    

  @commands.command(name='unmute',help='Send someone to purgatory')
  @commands.has_permissions(administrator=True)
  @is_in_guild([612845460360527883])
  async def unmute(self,ctx, member:discord.Member):
    remrole = discord.utils.get(member.guild.roles, name="Muted")
    try:
      await discord.Member.remove_roles(member, remrole)
    except:
      await ctx.send('That user isn\'t muted!')
    embed=discord.Embed(title=f"*{member.name+'#'+member.discriminator} was unmuted*", color=0x00ffaa)
    await ctx.send(embed=embed)


  @commands.group(name='exemption',help='Autorespond exemption command header',aliases=['ex'])
  @commands.has_permissions(administrator=True)
  async def exempt(self,ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send('Look at the subcommands list, random, and write and *help one of them')

  @exempt.command(name='add',help='exempts the channel you are in from autoresponse')
  async def add(self,ctx):
    author = ctx.author
    if author.guild_permissions.administrator:
      liste = []

      with open('json/exempt.txt','r') as filey:
        for blah in filey:
          liste.append(blah.strip())
      with open('json/exempt.txt','a') as filey:
        if str(ctx.channel.id) in liste:
          await ctx.send("This channel is already exempted from autoresponses.")
        else:
          filey.write(str(ctx.channel.id) + '\n')
          await ctx.send("Exempted. You will no longer receive autoresponses in this channel.")
        filey.close()
    else:
      embed = discord.Embed()
      await show_permission_error(ctx, embed)

  @exempt.command(name='remove',help='unexempts the channel you are in from autoresponse',aliases=['rem'])
  async def unexempt(self,ctx):
    author = ctx.author
    if author.guild_permissions.administrator:
      liste = []

      with open('json/exempt.txt','r') as filey:
        for blah in filey:
          liste.append(blah.strip())
      with open('json/exempt.txt','r+') as filey:
        filey.truncate(0)
        filey.close()

      if str(ctx.channel.id) in liste:

        uwu = str(ctx.channel.id)
        liste.remove(uwu)

        filey = open('json/exempt.txt','a')

        for lol in liste:
          print(lol)
          filey.write(str(lol) + '\n')
        await ctx.send("Unexempted. You will now receive autoresponses in this channel.")
      else:
        filey = open('json/exempt.txt','a')

        for lol in liste:
          print(lol)
          filey.write(str(lol) + '\n')
        await ctx.send("This channel is already allows autoresponses.")
        filey.close()


    else:
      embed = discord.Embed()
      await show_permission_error(ctx, embed)


  @commands.command(name='disperse',help='Randomly moves everyone in your vc to different ones')
  @commands.has_permissions(administrator=True)
  async def disperse(self,ctx):
    chans = []
    for x in ctx.guild.channels:
      if str(x)[:2]=='vc':
        chans.append(x)
    for members in ctx.author.voice.channel.members:
        await members.move_to(random.choice(chans))
  
  @commands.command(name='move',help='moves everyone in the vc to the vc specified')
  @commands.cooldown(1, 5, commands.BucketType.default)
  async def move(self, ctx, *, channel : discord.VoiceChannel):
    author = ctx.author
    if author.guild_permissions.move_members:
      numppl=0
      for members in ctx.author.voice.channel.members:
          numppl+=1
          await members.move_to(channel)
      embed = discord.Embed(color=discord.Color.red())
      embed.set_author(name=f"Moved {numppl} user(s) to {channel}")
      embed.clear_fields()
      await ctx.send(embed=embed)
    else:
      await show_permission_error(ctx, embed)

  @commands.command(name='send',help='send a message in the channel from the bot')
  @commands.has_permissions(administrator=True)
  async def send(self,ctx,*,msg:str):
    await ctx.send(msg)
    lmsg = await ctx.fetch_message(ctx.message.id)
    await lmsg.delete()
    print(ctx.author + ': ' + msg)
  
  @commands.command(name='reply',help='reply to a message given an id | Type "True" at the end and it will ping them as well')
  @commands.has_permissions(administrator=True)
  async def reply(self,ctx,msgid:int,*,msg:str):
    # print('hi')
    msgobj = await ctx.fetch_message(msgid)
    # print('hi')
    # await msgobj.send(msg)


    z=False
    if msg[-4:] == 'True':
      msg = msg[:-4]
      z=True
    
    if z:
      await msgobj.reply(msg, mention_author=True)
    else:
      await msgobj.reply(msg, mention_author=False)

    lmsg = await ctx.fetch_message(ctx.message.id)
    await lmsg.delete()
  


  @commands.command(name='move_message', help='Moves a message to a specific channel; takes parameters of messageID and channelID (to send it to)', aliases=["mm"])
  @commands.has_permissions(administrator=True)
  async def mooo(self, ctx, msg:discord.Message, channe:discord.TextChannel, ping=False):
    await channe.send("> " + str(msg.content))
    thingie = msg.author.id
    if ping or ping=="true":
      await channe.send('<@' + str(thingie) + '>')
    else:
      await channe.send(msg.author)
    await msg.delete()
    lmsg = await ctx.fetch_message(ctx.message.id)
    await lmsg.delete()

  async def show_common_error(ctx, embed, e):
    embed.clear_fields()
    embed.add_field(name=f"Something went wrong ({e})", value="")
    await ctx.send(embed=embed)


  async def show_permission_error(ctx, embed):
    embed.clear_fields()
    embed.add_field(name="No Permission", value="Make sure I have the necessary permissions.")
    await ctx.send(embed=embed)



  # mutes everyone in the current voice channel and un-mutes the bots
  @commands.command(name='smute',help='Mutes everyone in the voice channel',aliases=['ma'])
  @commands.cooldown(1, 5, commands.BucketType.default)
  async def smute(self,ctx,save='ok'):
      author = ctx.author  # command author
      embed = discord.Embed(color=discord.Color.red())

      if ctx.guild:  # check if the msg was in a server's text channel
          if author.voice:  # check if the user is in a voice channel
              if author.guild_permissions.mute_members:  # check if the user has deafen members permission
                  try:
                      no_of_members = 0
                      for member in author.voice.channel.members:  # traverse through the members list in current vc
                          if save.lower()=='save':
                                
                              if not get(member.roles, name="adminrole"):
                                await member.edit(mute=True)  
                                no_of_members += 1
                                
                          else:
                                
                              await member.edit(mute=True)  
                              no_of_members += 1


                      if no_of_members == 0:
                          embed.clear_fields()
                          embed.set_author(name="Everyone, please reconnect to the voice channel (or everyone was admin)")
                          
                      else:
                          embed.clear_fields()
                          embed.set_author(name=f"Deafened {no_of_members} user(s)")
                      await ctx.send(embed=embed)

                  except discord.Forbidden:
                      await show_permission_error(ctx, embed)
                  except Exception as e:
                      await show_common_error(ctx, embed, e)
              else:
                  await ctx.channel.send("You don't have the `Deafen Members` permission.")
          else:
              await ctx.send("You must join a voice channel first.")
      else:
          await ctx.send("This does not work in DMs.")

  @commands.command(name='deafen',help='Deafens everyone in the voice channel',aliases=['def'])
  @commands.cooldown(1, 5, commands.BucketType.default)
  async def deafen(self,ctx,save='ok'):
      author = ctx.author
      embed = discord.Embed(color=discord.Color.red())

      if ctx.guild:  # check if the msg was in a server's text channel
          if author.voice:  # check if the user is in a voice channel
              if author.guild_permissions.deafen_members:  # check if the user has deafen members permission
                  try:
                      no_of_members = 0
                      for member in author.voice.channel.members:  # traverse through the members list in current vc
                          if save.lower()=='save':
                                
                              if not get(member.roles, name="adminrole"):
                                await member.edit(deafen=True)  
                                no_of_members += 1
                                
                          else:
                                
                              await member.edit(deafen=True)  
                              no_of_members += 1


                      if no_of_members == 0:
                          embed.clear_fields()
                          embed.set_author(name="Everyone, please reconnect to the voice channel (or everyone was admin)")
                          
                      else:
                          embed.clear_fields()
                          embed.set_author(name=f"Deafened {no_of_members} user(s)")
                      await ctx.send(embed=embed)

                  except discord.Forbidden:
                      await show_permission_error(ctx, embed)
                  except Exception as e:
                      await show_common_error(ctx, embed, e)
              else:
                  await ctx.channel.send("You don't have the `Deafen Members` permission.")
          else:
              await ctx.send("You must join a voice channel first.")
      else:
          await ctx.send("This does not work in DMs.")


  # un-mutes everyone in the current voice channel and mutes the bots
  @commands.command(name='unsmute',help='Unmutes everyone in the voice channel',aliases=['uma'])
  async def unsmute(self,ctx):
      author = ctx.author  # command author
      embed = discord.Embed(color=discord.Color.green())

      if ctx.guild:  # check if the msg was in a server's text channel
          if author.voice:  # check if the user is in a voice channel
              try:
                  no_of_members = 0
                  for member in author.voice.channel.members:  # traverse through the members list in current vc
                      if not member.bot:  # check if member is not a bot
                          await member.edit(mute=False)  # unmute the non-bot member
                          no_of_members += 1
                  if no_of_members == 0:
                      embed.clear_fields()
                      embed.set_author(name="Everyone, please reconnect to the voice channel.")
                      # embed.add_field(name="Error", value="Everyone, please reconnect to the voice channel.")
                  else:
                      embed.clear_fields()
                      embed.set_author(name=f"Un-muted {no_of_members} user(s)")
                      # embed.add_field(name="Status", value=f"Muted {no_of_members} users.")
                  await ctx.send(embed=embed)

              except discord.Forbidden: # the bot doesn't have the permission to mute
                  await show_permission_error(ctx, embed)
              except Exception as e:
                  await show_common_error(ctx, embed, e)
          else:
              embed.clear_fields()
              embed.add_field(name="Error", value="You must join a voice channel first.")
              await ctx.send(embed=embed)
      else:
          embed.clear_fields()
          embed.add_field(name="Error", value="This does not work in DMs.")
          await ctx.send(embed=embed)


  # un-deafens everyone in the current voice channel
  @commands.command(name='undeafen',help='Undeafens everyone in the voice channel',aliases=["undef"])
  async def undeafen(self,ctx):
      author = ctx.author
      embed = discord.Embed(color=discord.Color.green())

      if ctx.guild:  # check if the msg was in a server's text channel
          if author.voice:  # check if the user is in a voice channel
              if author.guild_permissions.deafen_members:  # check if the user has deafen members permission
                  try:
                      no_of_members = 0
                      for member in author.voice.channel.members:  # traverse through the members list in current vc
                          await member.edit(deafen=False)  # un-deafen the member
                          no_of_members += 1
                      if no_of_members == 0:
                          embed.clear_fields()
                          embed.set_author(name="Everyone, please reconnect to the voice channel.")
                          
                      else:
                          embed.clear_fields()
                          embed.set_author(name=f"Undeafened {no_of_members} user(s)")
                      await ctx.send(embed=embed)

                  except discord.Forbidden:
                      await show_permission_error(ctx, embed)
                  except Exception as e:
                      await show_common_error(ctx, embed, e)
              else:
                  await ctx.channel.send("You don't have the `Mute Members` permission.")
          else:
              await ctx.send("You must join a voice channel first.")
      else:
          await ctx.send("This does not work in DMs.")

  @commands.command(name='disconnect',help='Disconnects everyone in the voice channel',aliases=["dc"])
  @commands.cooldown(1, 5, commands.BucketType.default)
  async def disconnect(self,ctx,save='ok'):
      author = ctx.author
      embed = discord.Embed(color=discord.Color.red())

      if ctx.guild:  # check if the msg was in a server's text channel
          if author.voice:  # check if the user is in a voice channel
              if author.guild_permissions.move_members:  # check if the user has deafen members permission
                  try:
                      no_of_members = 0
                      for member in author.voice.channel.members:  
                          if save.lower()=='save':
                                
                              if not get(member.roles, name="adminrole"):
                                await member.move_to(None)  
                                no_of_members += 1
                                
                          else:
                            
                            await member.move_to(None)  
                            no_of_members += 1
                          
                            

                      if no_of_members == 0:
                          embed.clear_fields()
                          embed.set_author(name="Everyone, please reconnect to the voice channel (or everyone was admin)")
                          
                      else:
                          embed.clear_fields()
                          embed.set_author(name=f"Disconnected {no_of_members} user(s)")
                      await ctx.send(embed=embed)

                  except discord.Forbidden:
                      await show_permission_error(ctx, embed)
                  except Exception as e:
                      await show_common_error(ctx, embed, e)
              else:
                  await ctx.channel.send("You don't have the `Disconnect Members` permission.")
          else:
              await ctx.send("You must join a voice channel first.")
      else:
          await ctx.send("This does not work in DMs.")

def setup(bot: commands.Bot):
    bot.add_cog(MODERATION(bot))






