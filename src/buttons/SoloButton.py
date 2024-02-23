__package__ = "buttons"

import nextcord
from nextcord import Interaction
from nextcord.ext import menus


class SoloButton(menus.ButtonMenu):
    def __init__(self):
        super().__init__()
        self.value = None

    async def send_initial_message(self, interaction):
        return await interaction.response.send_message(f'Signup')

    @nextcord.ui.button(emoji="\N{THUMBS UP SIGN}")
    async def on_thumbs_up(self, button, interaction):
        await self.message.edit(content=f"Thanks {interaction.user}!")

    