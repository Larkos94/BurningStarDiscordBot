import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs.SignupCog import SignupCog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

#intents = discord.Intents.messages

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

async def load():
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            if filename == '__init__.py':
                continue
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')


async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())

