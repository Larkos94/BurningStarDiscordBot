__package__ = "cogs"

import os
import nextcord
from nextcord.ext import commands

class SignupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @nextcord.slash_command(name = 'signup', description = 'Sign up for the event', guild_ids = [os.getenv('GUILD_ID')])
    async def signup(self, ctx):
        await ctx.send('You have signed up!')


def setup(bot : commands.Bot):
    bot.add_cog(SignupCog(bot))