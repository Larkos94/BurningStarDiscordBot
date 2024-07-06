__package__ = "models"

import jsonpickle
from models.EventModel import EventModel
from helpers.FileHelper import check_file, id_generator

class UpperEventModel(EventModel):
    def __init__(self, day, hour, minute, month, year, data, discription = ""):
        super().__init__(day, hour, minute, month, year, "UpperStaff Signup", data, discription)

        self.path = './src/files/uppersignup/'
        self.filename = id_generator()
        while check_file(self.path, self.filename):
            self.filename = id_generator()

        if data is None:
            self.hostaccount = []
            self.coordinator = []   
        else:
            self.hostaccount = data['hostaccount']
            self.coordinator = data['coordinator']

    def get_filename(self):
        return self.filename

    def get_signups(self):
        return [self.hostaccount, 
                self.coordinator
                ]

    def signup_solo(self, user):
        if user.name in self.hostaccount:
            self.hostaccount.remove(user.name)
            self.save_in_file()
            return False
        self.hostaccount.append(user.name)
        self.save_in_file()
        return True
    
    def signup_second_solo(self, user):
        if user.name in self.coordinator:
            self.coordinator.remove(user.name)
            self.save_in_file()
            return False
        self.coordinator.append(user.name)
        self.save_in_file()
        return True
    
    def save_in_file(self):

        data = {
            'hostaccount': self.hostaccount,
            'coordinator': self.coordinator,
            'day': self.day,
            'hour': self.hour,
            'minute': self.minute,
            'month': self.month,
            'year': self.year,
            'discription': self.discription
        }
        encoded = jsonpickle.encode(data)
        with open(self.path + self.filename + '.json', 'w+') as f:
            f.write(encoded)
        