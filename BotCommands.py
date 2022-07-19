import discord
from discord.ext import commands
import apiKeys
import requests
import json
intents = discord.Intents.default()
intents.members = True

client  = commands.Bot(command_prefix='$',intents=intents)



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
       
        