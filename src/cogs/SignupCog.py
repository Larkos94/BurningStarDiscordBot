__package__ = "cogs"

import os
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.ext import menus

from helpers.TimeHelper import get_month, get_year
from helpers.FileHelper import check_file, get_file
from menues.NormalEventMenu import NormalEventMenu
from menues.SoloEventMenu import SoloEventMenu
from menues.UpperEventMenu import UpperEventMenu

class SignupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
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
        normal_event = NormalEventMenu(self.bot, day, hour, minute, month, year, discription)
        await normal_event.start(interaction = interaction, ctx = None)
        normal_event.register_id()
        
    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
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

        solo_event = SoloEventMenu(self.bot, day, hour, minute, month, year, discription)
        await solo_event.start(interaction = interaction, ctx = None)
        solo_event.register_id()

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
    async def signup_upper(self, interaction: Interaction, 
                     day: int = SlashOption(name = 'day'),
                     hour: int = SlashOption(name = 'hour'),
                     minute: int = SlashOption(name = 'minute'),
                     month: int = SlashOption(name = 'month', required = False),
                     year: int = SlashOption(name = 'year', required = False)):

        if month is None:
            month = get_month()
        if year is None:
            year = get_year()
        upper_event = UpperEventMenu(self.bot, day, hour, minute, month, year)
        await upper_event.start(interaction = interaction, ctx = None)
        upper_event.register_id()

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
    async def restore_solo(self, interaction: Interaction, 
                     code: str = SlashOption(name = 'backupcode'),
                     ):
        path = './src/files/solosignup/'
        if not check_file(path, code):
            await interaction.response.send_message("No backup found")
            return
        
        data = get_file(path, code)
        solo_event = SoloEventMenu(self.bot, data['day'], data['hour'], data['minute'], data['month'], data['year'], data['discription'], data)
        await solo_event.start(interaction = interaction, ctx = None)
        solo_event.register_id()

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
    async def restore_normal(self, interaction: Interaction, 
                     code: str = SlashOption(name = 'backupcode'),
                     ):
        path = './src/files/normalsignup/'
        if not check_file(path, code):
            await interaction.response.send_message("No backup found")
            return
        
        data = get_file(path, code)
        normal_event = NormalEventMenu(self.bot, data['day'], data['hour'], data['minute'], data['month'], data['year'], data['discription'], data)
        await normal_event.start(interaction = interaction, ctx = None)
        normal_event.register_id()

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))], default_member_permissions= 268435456)
    async def restore_upper(self, interaction: Interaction, 
                     code: str = SlashOption(name = 'backupcode'),
                     ):
        path = './src/files/uppersignup/'
        if not check_file(path, code):
            await interaction.response.send_message("No backup found")
            return
        
        data = get_file(path, code)
        upper_event = UpperEventMenu(self.bot, data['day'], data['hour'], data['minute'], data['month'], data['year'], data)
        await upper_event.start(interaction = interaction, ctx = None)
        upper_event.register_id()

def setup(bot : commands.Bot):
    bot.add_cog(SignupCog(bot))