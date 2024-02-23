__package__ = "cogs"

import os
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.ext import menus

from helpers.TimeHelper import get_timestamp, get_day_name
from views.SignupView import SignupView
from buttons.SoloButton import SoloButton

class SignupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(guild_ids = [int(os.getenv('GUILD_ID'))])
    async def signup(self, interaction: Interaction, 
                     day: int = SlashOption(name = 'day'),
                     hour: int = SlashOption(name = 'hour'),
                     minute: int = SlashOption(name = 'minute')):
        day_name = day
        if hour-6 < 0:
            day_name = day_name - 1
        view = SignupView(get_timestamp(day, hour, minute),  get_day_name(day_name, hour, minute))

        await interaction.send(embed = view.embeded_create())
        
        await SoloButton().start(interaction)

def setup(bot : commands.Bot):
    bot.add_cog(SignupCog(bot))