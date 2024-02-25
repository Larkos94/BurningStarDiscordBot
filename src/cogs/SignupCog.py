__package__ = "cogs"

import os
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.ext import menus

from helpers.TimeHelper import get_month, get_year
from menues.NormalEventMenu import NormalEventMenu
from menues.SoloEventMenu import SoloEventMenu

class SignupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID')), int(os.getenv('GUILD_ID2'))], default_member_permissions= 268435456)
    async def signup_normal(self, interaction: Interaction, 
                     day: int = SlashOption(name = 'day'),
                     hour: int = SlashOption(name = 'hour'),
                     minute: int = SlashOption(name = 'minute'),
                     month: int = SlashOption(name = 'month', required = False),
                     year: int = SlashOption(name = 'year', required = False),
                     discription: str = SlashOption(name = 'discription', required = False)):

        if discription is None:
            discription = ""
        if month is None:
            month = get_month()
        if year is None:
            year = get_year()
        await NormalEventMenu(day, hour, minute, month, year, discription).start(interaction = interaction, ctx = None)
        
    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID')), int(os.getenv('GUILD_ID2'))], default_member_permissions= 268435456)
    async def signup_solo(self, interaction: Interaction, 
                     day: int = SlashOption(name = 'day'),
                     hour: int = SlashOption(name = 'hour'),
                     minute: int = SlashOption(name = 'minute'),
                     month: int = SlashOption(name = 'month', required = False),
                     year: int = SlashOption(name = 'year', required = False),
                     discription: str = SlashOption(name = 'discription', required = False)):

        if discription is None:
            discription = ""
        if month is None:
            month = get_month()
        if year is None:
            year = get_year()
        await SoloEventMenu(day, hour, minute, month, year, discription).start(interaction = interaction, ctx = None)

def setup(bot : commands.Bot):
    bot.add_cog(SignupCog(bot))