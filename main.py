#required dependicies
import discord
from discord.ext import commands
import requests
import json
from youtubesearchpython import *
import os
import DiscordUtils


from music_cog import music_cog

intents = discord.Intents.default()
intents.members = True
music = DiscordUtils.Music()
bot  = commands.Bot(command_prefix='$',intents=intents)

bot.add_cog(music_cog(bot,music))
# bot.add_cog(helper_cog(bot))





#make bot leave from voice channel 
@bot.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Doby must leave voice channel !")
    else:
        await ctx.send("Doby not in a voice channel")


@bot.command(pass_context=True)
async def ytplay(ctx,url:str):
    try:
        video = Video.get(url, mode = ResultMode.json, get_upload_date=True)
        print(type(video))
        print(video)
        thumbnails = video.get('thumbnails') 
        # json_formated_str = json.dumps(video,indent=2)
        # print(json_formated_str)
        embed = discord.Embed(title=video.get('title'),url=video.get('link'))
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        embed.add_field(name='Publish Date',value=video.get('publishDate'),inline=True)
        embed.add_field(name='View Count',value=video.get('viewCount')['text'],inline=True)
        for thumb in thumbnails:
            embed.set_thumbnail(url=thumb['url'])

        await ctx.send(embed=embed)
    except:
        await ctx.send('Master Your link is invalid,Please check again')



@bot.event
async def on_ready():
    print("The Bot is now ready for use!")
    print(".........................")


bot.run('OTk4MjE0MDA1Nzg3MjA5NzU4.GGsWiI.UNvdUGLR5OnpeU8VJpJOZhVzp8AEYdCm_E6_24')