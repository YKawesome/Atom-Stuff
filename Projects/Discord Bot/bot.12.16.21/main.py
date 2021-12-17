# bot.py
import os
import discord
import keep_alive

from dotenv import load_dotenv

keep_alive.keep_alive()
# 1
from discord.ext import commands

description = "A bot that has many unique purposes, for many unique things."

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

startup_extensions = [
    "fun", "moderation", "school", "info", "quotes", "autorespond"
]

# startup_extensions = ["school", "info"]

# 2
bot = commands.Bot(command_prefix='*', description=description)


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.listening, name="*help"))
	print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send(
		    'You do not have the correct role for this command, or you are in the wrong server.'
		)
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send('This command is on a %.2fs cooldown' %
		               error.retry_after)


if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

	bot.run(TOKEN)

# for file in os.listdir("/home/user/bot/commands"):
#     if file.endswith(".py"):
#         client.load_extension(f'commands.{file[:-3]}')
