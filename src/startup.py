import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

#intents = discord.Intents.messages

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_message(message):
    if 'ping' in message.content.lower():
        await message.channel.send('Pong!')

client.run(TOKEN)

