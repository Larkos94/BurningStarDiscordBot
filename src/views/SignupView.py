__package__ = "views"

import nextcord
from nextcord import Embed

class SignupView():
    def __init__(self, discord_timestamp: str, day_name: str = None):
        self.day_name = day_name
        self.embeded = Embed(title = "Signup " + day_name, description = "Eventsignup")
        self.timestamp = discord_timestamp
    
    def embeded_create(self):

        self.set_colour()
        self.embeded.add_field(name = "Your local time: ", value = self.timestamp)
        self.embeded.add_field(name = "Event", value = "Event BLA BLA BLA", inline=False)
        return self.embeded
    
    def set_colour(self):

        match self.day_name:

            case "Monday":
                self.embeded.colour = nextcord.Colour.red()
            case "Tuesday":
                self.embeded.colour = nextcord.Colour.orange()
            case "Wednesday":
                self.embeded.colour = nextcord.Colour.gold()
            case "Thursday":
                self.embeded.colour = nextcord.Colour.green()
            case "Friday":
                self.embeded.colour = nextcord.Colour.blue()
            case "Saturday":
                self.embeded.colour = nextcord.Colour.purple()
            case "Sunday":
                self.embeded.colour = nextcord.Colour.magenta()
            
        return
            
        
    