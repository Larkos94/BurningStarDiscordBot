__package__ = "views"

import nextcord
from nextcord import Embed

from views.EventView import EventView

class SigneupCloseView(EventView):
    def __init__(self, discord_timestamp, event_day, singups, event_type, discription, roles):
        super().__init__(discord_timestamp, event_day, singups, event_type, discription)
        self.roles = roles
        self.embeded = Embed(title = "Event Signup for " + event_day + " is closed!")

    def embeded_create(self):
        self.embeded.colour = self.get_colour()
        self.embeded.set_image("https://cdn.discordapp.com/attachments/827147397184487456/1211101174195949628/closed.jpg?ex=65ecf8dd&is=65da83dd&hm=fecf0cba5963e4d35200c0440c78a13fd481fa6968ad0040c920e842045e2296&")
        self.embeded.add_field(name = "Your local time: ", value = self.timestamp, inline=False)
        self.embeded.add_field(name = "Event Type", value = self.event_type, inline=False)
        if self.discription != "":
            self.embeded.add_field(name = "Event details", value = '', inline=False)

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
        self.embeded.add_field(name = "If you still like to join DM: ", value = "Firedragon, Lia or Larkos")

        return self.embeded
    

    def generate_user_string(self, userlist):
        user_string = ""
        for user in userlist:
            user_string += str(user) + "\n"
        user_string += "------------\n"
        return user_string
        