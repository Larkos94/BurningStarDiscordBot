__package__ = "menues"

import os
import nextcord
from nextcord import Interaction
from nextcord.ext import menus

from views.SoloEventView import SoloEventView
from views.SigneupCloseView import SigneupCloseView
from models.SoloEventModel import SoloEventModel

class SoloEventMenu(menus.ButtonMenu):
    def __init__(self, bot, day, hour, minute, month, year, discription):
        super().__init__(timeout=1209600)
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year
        self.discription = discription
        self.model = SoloEventModel(day, hour, minute, month, year)
        self.discord_message_id = None
        self.discord_channel_id = None
        self.closed = False

    async def send_initial_message(self, ctx, channel):
        view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.interaction.response.send_message(embed = view.embeded_create(), view=self)
        return await self.interaction.original_message()
    
    def register_id(self):
        self.discord_message_id = self.message.id
        self.discord_channel_id = self.message.channel.id
    
    @nextcord.ui.button(label='Solo', style=nextcord.ButtonStyle.primary)
    async def on_solo(self, button, interaction):
        if self.closed is False:
            self.model.signup_solo(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Second Solo', style=nextcord.ButtonStyle.primary)
    async def on_second_solo(self, button, interaction):
        if self.closed is False:
            self.model.signup_second_solo(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Floater', style=nextcord.ButtonStyle.primary)
    async def on_floater(self, button, interaction):
        if self.closed is False:
            self.model.signup_floater(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Security', style=nextcord.ButtonStyle.primary)
    async def on_security(self, button, interaction):
        if self.closed is False:
            self.model.signup_security(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Host', style=nextcord.ButtonStyle.primary)
    async def on_mc(self, button, interaction):
        if self.closed is False:
            self.model.signup_mc(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='DJ', style=nextcord.ButtonStyle.primary)
    async def on_dj(self, button, interaction):
        if self.closed is False:
            self.model.signup_dj(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Backup Dancer', style=nextcord.ButtonStyle.primary)
    async def on_backup_dancer(self, button, interaction):
        if self.closed is False:
            self.model.signup_backup_dancer(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(label='Backup Staff', style=nextcord.ButtonStyle.primary)
    async def on_backup_staff(self, button, interaction):
        if self.closed is False:
            self.model.signup_backup_staff(interaction.user)
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            await self.send_message(view)
        else:
            pass

    @nextcord.ui.button(emoji="\N{KEY}", style=nextcord.ButtonStyle.green)
    async def on_close(self, button, interaction):
        if nextcord.utils.get(interaction.guild.roles, name=os.getenv('SIGNUP_ROLE')) in interaction.user.roles:
            view = SoloEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            if self.closed:
                self.closed = False 
            else:
                self.closed = True
                view = SigneupCloseView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), 
                                        self.model.get_event_type(), self.discription, view.get_roles())
            
            await self.send_message(view, content=f"Event was closed by {interaction.user}!")
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