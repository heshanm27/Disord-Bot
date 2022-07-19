
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import DiscordUtils
class music_cog(commands.Cog):
    def __init__(self, bot,music):
        self.bot = bot
        self.music = music
        #all the music related stuff
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

     #searching the item on youtube
    @commands.command(pass_context=True)
    async def join(self,ctx):
        if(ctx.author.voice):
            channel =ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Master not in a voice channel,Doby can't join")


    @commands.command()
    async def play(self,ctx, *, url):
        await self.join(ctx)
        player = self.music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = self.music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f"Playing {song.name}")
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f"Queued {song.name}")