__package__ = "cogs"

import os
import nextcord
from helpers.TimeHelper import get_timestamp, get_month, get_year
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands

class PublicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID')), int(os.getenv('GUILD_ID2'))])
    async def time(self, interaction: Interaction, 
                   day: int = SlashOption(name = 'day'),
                   hour: int = SlashOption(name = 'hour'),
                   minute: int = SlashOption(name = 'minute'),
                   month: int = SlashOption(name = 'month', required = False),
                   year: int = SlashOption(name = 'year', required = False)):
        
        if month is None:
            month = get_month()
        if year is None:
            year = get_year()

        await interaction.response.send_message(get_timestamp(day, hour, minute))

def setup(bot : commands.Bot):
    bot.add_cog(PublicCog(bot))