import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith('$hello'):
        await message.channel.send('hello!')

client.run(os.getenv('TOKEN'))
