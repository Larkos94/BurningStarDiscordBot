__package__ = "menues"

import nextcord
from nextcord import Interaction
from nextcord.ext import menus

from views.SignupView import SignupView
from helpers.TimeHelper import get_timestamp, get_day_name

class NormalEventMenu(menus.ButtonMenu):
    def __init__(self, day, hour, minute):
        super().__init__()
        self.discord_timestamp = get_timestamp(day, hour, minute)
        self.day_name = get_day_name(day, hour, minute)

    async def send_initial_message(self, ctx, channel):
        view = SignupView(self.discord_timestamp, self.day_name)
        await self.interaction.response.send_message(embed = view.embeded_create(), view=self)
        return await self.interaction.original_message()
    
    @nextcord.ui.button(emoji="\N{NO ENTRY SIGN}")
    async def on_cancel(self, button, interaction):
        await self.message.edit(content=f"Event was canceled by {interaction.user}!", embed=None)