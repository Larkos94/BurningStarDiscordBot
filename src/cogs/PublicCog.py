__package__ = "cogs"

import os
import nextcord
from helpers.TimeHelper import get_timestamp
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands

class PublicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))])
    async def time(self, interaction: Interaction, 
                   day: int = SlashOption(name = 'day'),
                   hour: int = SlashOption(name = 'hour'),
                   minute: int = SlashOption(name = 'minute')):
        await interaction.response.send_message(get_timestamp(day, hour, minute))

def setup(bot : commands.Bot):
    bot.add_cog(PublicCog(bot))