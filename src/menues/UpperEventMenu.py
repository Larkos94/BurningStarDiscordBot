__package__ = "menues"

import os
import nextcord
from nextcord import Interaction
from nextcord.ext import menus

from views.UpperEventView import UpperEventView
from views.SigneupCloseView import SigneupCloseView
from models.UpperEventModel import UpperEventModel

class UpperEventMenu(menus.ButtonMenu):
    def __init__(self, bot, day, hour, minute, month, year, data=None):
        super().__init__(timeout=1209600)
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year
        self.discription = ""
        self.data = data
        self.model = UpperEventModel(day, hour, minute, month, year, data)
        self.restore_code = self.model.get_filename()
        self.discord_message_id = None
        self.discord_channel_id = None
        self.closed = False

    async def send_initial_message(self, ctx, channel):
        view = UpperEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription, self.restore_code)
        await self.interaction.send(embed = view.embeded_create(), view=self)
        return await self.interaction.original_message()
    
    def register_id(self):
        self.discord_message_id = self.message.id
        self.discord_channel_id = self.message.channel.id
    
    @nextcord.ui.button(label='Host Account', style=nextcord.ButtonStyle.primary)
    async def on_solo(self, button, interaction):
        if self.closed is False:
            self.model.signup_solo(interaction.user)
            view = UpperEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription, self.restore_code)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Coordinator', style=nextcord.ButtonStyle.primary)
    async def on_second_solo(self, button, interaction):
        if self.closed is False:
            self.model.signup_second_solo(interaction.user)
            view = UpperEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription, self.restore_code)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(emoji="\N{NO ENTRY SIGN}")
    async def on_cancel(self, button, interaction):
        if nextcord.utils.get(interaction.guild.roles, name=os.getenv('CANCEL_ROLE')) in interaction.user.roles:
            self.closed = True
            await self.send_message(view = None, content=f"Event was canceled by {interaction.user}!")
        else:
            pass

    async def send_message(self, view, content=None):
        channel = self.bot.get_channel(self.discord_channel_id)
        message = await channel.fetch_message(self.discord_message_id)
        if view is None:
            await message.edit(content=content, embed=None)
        else: 
            await message.edit(embed=view.embeded_create(), content=content)