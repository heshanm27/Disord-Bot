#required dependicies
import discord
from discord.ext import commands
import requests
import json
from youtubesearchpython import *
import os


from help_cog import help_cog
from music_cog import music_og

intents = discord.Intents.default()
intents.members = True

bot  = commands.Bot(command_prefix='$',intents=intents)

bot.add_cog(music_cog(bot))
bot.add_cog(helper_cog(bot))



bot.run(os.getenv("BotApiToken"))