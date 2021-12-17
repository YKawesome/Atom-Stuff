# import asyncio
# import functools
# import itertools
# import math
# import random

# import discord
# import youtube_dl
# from async_timeout import timeout
# from discord.ext import commands

# # Silence useless bug reports messages
# youtube_dl.utils.bug_reports_message = lambda: ''


# class VoiceError(Exception):
#     pass


# class YTDLError(Exception):
#     pass


# class YTDLSource(discord.PCMVolumeTransformer):
#     YTDL_OPTIONS = {
#         'format': 'bestaudio/best',
#         'extractaudio': True,
#         'audioformat': 'mp3',
#         'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#         'restrictfilenames': True,
#         'noplaylist': True,
#         'nocheckcertificate': True,
#         'ignoreerrors': False,
#         'logtostderr': False,
#         'quiet': True,
#         'no_warnings': True,
#         'default_search': 'auto',
#         'source_address': '0.0.0.0',
#     }

#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#         'options': '-vn',
#     }

#     ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

# class MUSIC(commands.Cog,description="Miscellaneous/fun commands suggested by members"):
#   def __init__(self, bot, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
#     self.bot = bot
#     super().__init__(source, volume)

#     self.requester = ctx.author
#     self.channel = ctx.channel
#     self.data = data

#     self.uploader = data.get('uploader')
#     self.uploader_url = data.get('uploader_url')
#     date = data.get('upload_date')
#     self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
#     self.title = data.get('title')
#     self.thumbnail = data.get('thumbnail')
#     self.description = data.get('description')
#     self.duration = self.parse_duration(int(data.get('duration')))
#     self.tags = data.get('tags')
#     self.url = data.get('webpage_url')
#     self.views = data.get('view_count')
#     self.likes = data.get('like_count')
#     self.dislikes = data.get('dislike_count')
#     self.stream_url = data.get('url')
    

  


# def setup(bot: commands.Bot):
#     bot.add_cog(MUSIC(bot))