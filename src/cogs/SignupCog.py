__package__ = "cogs"

import asyncio
import os
import discord
from discord.ext import commands

class SignupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def signup(self, ctx):
        await ctx.send('You have signed up!')


async def setup(bot):
    await bot.add_cog(SignupCog(bot))