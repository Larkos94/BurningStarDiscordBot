__package__ = "views"

import nextcord
from nextcord import Embed

class EventView():
    def __init__(self, discord_timestamp, event_day, singups, event_type):
        self.embeded = Embed(title = "Signup " + event_day, description = "Eventsignup")
        self.timestamp = discord_timestamp
        self.event_day = event_day
        self.singups = singups
        self.event_type = event_type

    def get_colour(self):
        match self.event_day:

            case "Monday":
                return nextcord.Colour.red()
            case "Tuesday":
                return nextcord.Colour.orange()
            case "Wednesday":
                return nextcord.Colour.gold()
            case "Thursday":
                return nextcord.Colour.green()
            case "Friday":
                return nextcord.Colour.blue()
            case "Saturday":
                return nextcord.Colour.purple()
            case "Sunday":
                return nextcord.Colour.magenta()
            
        return nextcord.Colour.default()