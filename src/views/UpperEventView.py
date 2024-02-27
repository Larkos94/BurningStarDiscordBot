__package__ = "views"

import nextcord
from nextcord import Embed

from views.EventView import EventView

class UpperEventView(EventView):
    def __init__(self, discord_timestamp, event_day, singups, event_type, discription):
        super().__init__(discord_timestamp, event_day, singups, event_type, discription)
        self.roles = ["Host Account", "Coordinator"]

    def get_roles(self):
        return self.roles

    def embeded_create(self):
        self.embeded.colour = self.get_colour()
        self.embeded.add_field(name = "Your local time: ", value = self.timestamp)
        self.embeded.add_field(name = "Event Type", value = self.event_type, inline=False)
        if self.discription != "":
            self.embeded.add_field(name = "Event details", value = self.discription, inline=False)

        self.embeded.add_field(name = "+++++++++++++++++++++++++++++++++++++++++++++++++", value=" ", inline=False)
        index = 0
        first = False
        for singup in self.singups:
            
            
            user_string = self.generate_user_string(singup)
            self.embeded.add_field(name = self.roles[index] + " ["+ str(len(singup))+ "]", value = user_string, inline=first)
            index += 1

            if index > 0:
                first = False

        self.embeded.add_field(name = "+++++++++++++++++++++++++++++++++++++++++++++++++", value=" ", inline=False)

        return self.embeded
    
    def generate_user_string(self, userlist):
        user_string = ""
        for user in userlist:
            user_string += str(user) + "\n"
        user_string += "------------\n"
        return user_string
        