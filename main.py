import discord
from discord.ext import commands
import apiKeys
import requests
import json
intents = discord.Intents.default()
intents.members = True

client  = commands.Bot(command_prefix='$',intents=intents)

@client.event
async def on_ready():
    print("The Bot is now ready for use!")
    print(".........................")


#this is thw function user use for communiate with bot
@client.command()
async def hello(ctx):
    await ctx.send("Hello,I am doby the Bot (-_-) ")

@client.command()
async def joke(ctx):
        channel = client.get_channel(817985518650130467)
        await channel.send("here is a joke")
        _url = "https://random-stuff-api.p.rapidapi.com/joke"

        _querystring = {"tag":"men"}

        _headers = {
            "Authorization": apiKeys.jokesAuthorizekey,
            "X-RapidAPI-Key": apiKeys.JokesApiKey,
            "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com"
        }
        _response = requests.request("GET", _url, headers=_headers, params=_querystring)
        responseData = json.loads(_response.text)

        await channel.send(responseData['joke'])
       
        

@client.event
async def on_member_join(memebr):

        channel = client.get_channel(817985518650130467)
        await channel.send("Welcome bro, ready to spend time with bros")
        _url = "https://random-stuff-api.p.rapidapi.com/joke"

        _querystring = {"tag":"men"}

        _headers = {
            "Authorization": apiKeys.jokesAuthorizekey,
            "X-RapidAPI-Key": apiKeys.JokesApiKey,
            "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com"
        }
        _response = requests.request("GET", _url, headers=_headers, params=_querystring)
        responseData = json.loads(_response.text)
        await channel.send('Here is a joke for you')
        await channel.send(responseData['joke'])



client.run(apiKeys.BotApiToken)