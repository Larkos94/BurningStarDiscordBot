__package__ = "menues"

import nextcord
from nextcord import Interaction
from nextcord.ext import menus

from views.NormalEventView import NormalEventView
from helpers.TimeHelper import get_timestamp, get_day_name
from models.NormalEventModel import NormalEventModel

class NormalEventMenu(menus.ButtonMenu):
    def __init__(self, day, hour, minute):
        super().__init__()
        self.day = day
        self.hour = hour
        self.minute = minute
        self.model = NormalEventModel(day, hour, minute)

    async def send_initial_message(self, ctx, channel):
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.interaction.response.send_message(embed = view.embeded_create(), view=self)
        return await self.interaction.original_message()
    
    @nextcord.ui.button(label='Solo', style=nextcord.ButtonStyle.primary)
    async def on_solo(self, button, interaction):
        self.model.signup_solo(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())
    
    @nextcord.ui.button(label='Duo', style=nextcord.ButtonStyle.primary)
    async def on_duo(self, button, interaction):
        self.model.signup_duo(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Group', style=nextcord.ButtonStyle.primary)
    async def on_group(self, button, interaction):
        self.model.signup_group(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Floater', style=nextcord.ButtonStyle.primary)
    async def on_floater(self, button, interaction):
        self.model.signup_floater(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Security', style=nextcord.ButtonStyle.primary)
    async def on_security(self, button, interaction):
        self.model.signup_security(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Host', style=nextcord.ButtonStyle.primary)
    async def on_mc(self, button, interaction):
        self.model.signup_mc(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='DJ', style=nextcord.ButtonStyle.primary)
    async def on_dj(self, button, interaction):
        self.model.signup_dj(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Backup Dancer', style=nextcord.ButtonStyle.primary)
    async def on_backup_dancer(self, button, interaction):
        self.model.signup_backup_dancer(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())

    @nextcord.ui.button(label='Backup Staff', style=nextcord.ButtonStyle.primary)
    async def on_backup_staff(self, button, interaction):
        self.model.signup_backup_staff(interaction.user)
        view = NormalEventView(self.model.get_event_timestamp(), self.model.get_event_day(), self.model.get_signups(), self.model.get_event_type())
        await self.message.edit(embed=view.embeded_create())
    
    @nextcord.ui.button(emoji="\N{NO ENTRY SIGN}")
    async def on_cancel(self, button, interaction):
        await self.message.edit(content=f"Event was canceled by {interaction.user}!", embed=None)
        self.stop()