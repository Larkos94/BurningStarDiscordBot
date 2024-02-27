__package__ = "models"

import os
from models.EventModel import EventModel

class UpperEventModel(EventModel):
    def __init__(self, day, hour, minute, month, year):
        super().__init__(day, hour, minute, month, year, "UpperStaff Signup")
        self.hostaccount = []
        self.coordinator = []

    def get_signups(self):
        return [self.hostaccount, 
                self.coordinator
                ]

    def signup_solo(self, user):
        if user in self.hostaccount:
            self.hostaccount.remove(user)
            return False
        self.hostaccount.append(user)
        return True
    
    def signup_second_solo(self, user):
        if user in self.coordinator:
            self.coordinator.remove(user)
            return False
        self.coordinator.append(user)
        return True