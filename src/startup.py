import asyncio
import os
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import commands
from dotenv import load_dotenv
from cogs.SignupCog import SignupCog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


intents = nextcord.Intents.all()
intents.members = True
bot = commands.Bot(intents=intents, help_command=None)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.slash_command(guild_ids = [os.getenv('GUILD_ID')])
async def test(inter: Interaction):
    await inter.response.send_message('You have signed up!')

def load():
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            if filename == '__init__.py':
                continue
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')

load()

bot.run(TOKEN)



