__package__ = "views"

import nextcord
from nextcord import Embed

from views.EventView import EventView

class NormalEventView(EventView):
    def __init__(self, discord_timestamp, event_day, singups, event_type):
        super().__init__(discord_timestamp, event_day, singups, event_type)
        self.roles = ["Solo", "Duo", "Group", "Floater", "Security", "Host", "DJ", "Coordinator", "Backup_Dancer", "Backup_Staff"]

    def embeded_create(self):
        self.embeded.colour = self.get_colour()
        self.embeded.add_field(name = "Your local time: ", value = self.timestamp)
        self.embeded.add_field(name = "Event Type", value = self.event_type, inline=False)

        index = 0
        for singup in self.singups:
            first = False
            
            user_string = self.generate_user_string(singup)
            self.embeded.add_field(name = self.roles[index], value = user_string, inline=first)
            index += 1

            if index > 0:
                first = True

        return self.embeded
    
    def generate_user_string(self, userlist):
        #user_string = "{roletype}:\n \n"
        user_string = ""
        for user in userlist:
            user_string += str(user) + "\n"
        return user_string
        