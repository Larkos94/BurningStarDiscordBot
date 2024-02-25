__package__ = "menues"

import os
import nextcord
from nextcord import Interaction
from nextcord.ext import menus

from views.NormalEventView import NormalEventView
from views.SigneupCloseView import SigneupCloseView
from models.NormalEventModel import NormalEventModel

class NormalEventMenu(menus.ButtonMenu):
    def __init__(self, day, hour, minute, month, year, discription):
        super().__init__(timeout=1209600)
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year
        self.discription = discription
        self.model = NormalEventModel(day, hour, minute, month, year)

    async def send_initial_message(self, ctx, channel):
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.interaction.response.send_message(embed = view.embeded_create(), view=self)
        return await self.interaction.original_message()
    
    @nextcord.ui.button(label='Solo', style=nextcord.ButtonStyle.primary)
    async def on_solo(self, button, interaction):
        self.model.signup_solo(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())
    
    @nextcord.ui.button(label='Duo', style=nextcord.ButtonStyle.primary)
    async def on_duo(self, button, interaction):
        self.model.signup_duo(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Group', style=nextcord.ButtonStyle.primary)
    async def on_group(self, button, interaction):
        self.model.signup_group(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Floater', style=nextcord.ButtonStyle.primary)
    async def on_floater(self, button, interaction):
        self.model.signup_floater(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Security', style=nextcord.ButtonStyle.primary)
    async def on_security(self, button, interaction):
        self.model.signup_security(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Host', style=nextcord.ButtonStyle.primary)
    async def on_mc(self, button, interaction):
        self.model.signup_mc(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='DJ', style=nextcord.ButtonStyle.primary)
    async def on_dj(self, button, interaction):
        self.model.signup_dj(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Backup Dancer', style=nextcord.ButtonStyle.primary)
    async def on_backup_dancer(self, button, interaction):
        self.model.signup_backup_dancer(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Backup Staff', style=nextcord.ButtonStyle.primary)
    async def on_backup_staff(self, button, interaction):
        self.model.signup_backup_staff(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
        await self.message.edit(embed=view.embeded_create())
    
    @nextcord.ui.button(emoji="\N{KEY}", style=nextcord.ButtonStyle.green)
    async def on_close(self, button, interaction):
        if nextcord.utils.get(interaction.guild.roles, name=os.getenv('SIGNUP_ROLE')) in interaction.user.roles:
            view_old = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type(), self.discription)
            view = SigneupCloseView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), 
                                    self.model.get_event_type(), self.discription, view_old.get_roles())
            await self.message.edit(embed=view.embeded_create())
            self.stop()
        else:
            pass

    @nextcord.ui.button(emoji="\N{NO ENTRY SIGN}")
    async def on_cancel(self, button, interaction):
        if nextcord.utils.get(interaction.guild.roles, name=os.getenv('CANCEL_ROLE')) in interaction.user.roles:
            await self.message.edit(content=f"Event was canceled by {interaction.user}!", embed=None)
            self.stop()
        else:
            pass

        