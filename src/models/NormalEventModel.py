__package__ = "models"

import os
from models.EventModel import EventModel

class NormalEventModel(EventModel):
    def __init__(self, day, hour, minute, month, year):
        super().__init__(day, hour, minute, month, year, "Normal Event")
        self.dancer_solo = []
        self.dancer_duo = []
        self.dancer_group = []
        self.dancer_floater = []
        self.security = []
        self.mc = []
        self.dj = []
        self.backup_dancer = []
        self.backup_staff = []

    def get_signups(self):
        return [self.dancer_solo, 
                self.dancer_duo, 
                self.dancer_group, 
                self.dancer_floater, 
                self.security, 
                self.mc, 
                self.dj, 
                self.backup_dancer, 
                self.backup_staff
                ]

    def signup_solo(self, user):
        if user in self.dancer_solo:
            self.dancer_solo.remove(user)
            return False
        self.dancer_solo.append(user)
        return True
    
    def signup_duo(self, user):
        if user in self.dancer_duo:
            self.dancer_duo.remove(user)
            return False
        self.dancer_duo.append(user)
        return True
    
    def signup_group(self, user):
        if user in self.dancer_group:
            self.dancer_group.remove(user)
            return False
        self.dancer_group.append(user)
        return True

    def signup_floater(self, user):
        if user in self.dancer_floater:
            self.dancer_floater.remove(user)
            return False
        self.dancer_floater.append(user)
        return True

    def signup_security(self, user):
        if user in self.security:
            self.security.remove(user)
            return False
        self.security.append(user)
        return True

    def signup_mc(self, user):
        if user in self.mc:
            self.mc.remove(user)
            return False
        self.mc.append(user)
        return True
    
    def signup_dj(self, user):
        if user in self.dj:
            self.dj.remove(user)
            return False
        self.dj.append(user)
        return True
    
    def signup_coordinator(self, user):
        if user in self.coordinator:
            self.coordinator.remove(user)
            return False
        self.coordinator.append(user)
        return True
    
    def signup_backup_dancer(self, user):
        if user in self.backup_dancer:
            self.backup_dancer.remove(user)
            return False
        self.backup_dancer.append(user)

    def signup_backup_staff(self, user):
        if user in self.backup_staff:
            self.backup_staff.remove(user)
            return False
        self.backup_staff.append(user)
        return True
