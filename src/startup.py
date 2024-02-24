import os
import nextcord
from nextcord import Intents, Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = nextcord.Intents.all()
intents.members = True
bot = commands.Bot(
    "/", intents=Intents(messages=True, guilds=True, members=True, message_content=True)
)

def load():
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            if filename == '__init__.py':
                continue
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')



load()
bot.run(TOKEN)




